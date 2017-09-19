
import org.jenkinsci.plugins.workflow.steps.FlowInterruptedException

gitlabHost = '192.168.10.11'
gitlabCredential='gitlab-jetty-key'

releaseVersion = '0.9.38.0'
stableVersion = ''

deploymentEnv = 'test'
appHost = "devicehive:&${deploymentEnv}"
nginxHost = "web:&${deploymentEnv}"

projectRoot = '/opt/webapps/devicehive'
releaseRoot = '/opt/release/devicehive'
activate = ''

mailMessage = ''


try {

    node('docker-ansible') {

        stage('checkout scm') {
            git branch: 'master', credentialsId: "${gitlabCredential}", url: "git@${gitlabHost}:bbc/profile.git"
            // checkout scm
        }

        dir('devicehive') {
            def releaseDir = "${releaseRoot}/${releaseVersion}"

            stage('准备配置文件') {
                sh "ansible '${appHost}' -m file -a 'state=directory path=${releaseDir}/conf'"
                sh "ansible '${appHost}' -m copy -a 'src=${deploymentEnv}/ dest=${releaseDir}/conf/'"
            }

            stage('准备 artifact') {
                def server
                withCredentials([usernamePassword(credentialsId: 'artifact-repo', passwordVariable: 'pass', usernameVariable: 'user')]) {
                    server = Artifactory.newServer url: 'http://repo.d.bigbigcloud.cn:8081/artifactory', username: "${user}", password: "${pass}"
                }

                def downloadSpec = """
                {
                    "files": [{
                        "pattern": "bigbigcloud/*devicehive-${releaseVersion}-boot.jar",
                        "target": "devicehive.jar",
                        "flat": true
                    }]
                }
                """

                server.download(spec: downloadSpec)
                sh "ansible '${appHost}' -m copy -a 'src=devicehive.jar dest=${releaseDir}/'"
                sh "ansible '${appHost}' -m file -a 'state=link src=${releaseDir} dest=${releaseRoot}/latest'"
                stableVersion = sh(returnStdout: true, script: "ansible '${appHost}' -m command -a 'readlink -f ${releaseRoot}/stable' | tail -1 | xargs basename").trim()
            }

            def deployDir = "${projectRoot}"
            stage('准备部署') {
                sh "ansible '${appHost}' -m file -a 'state=directory path=${deployDir}'"
                sh "ansible '${appHost}' -m copy -a 'src=deploy/ dest=${deployDir}/'"
                sh "ansible '${appHost}' -m file -a 'path=${deployDir}/01-deploy.sh mode=u+x'"
                activate = sh(returnStdout: true, script: "ansible '${appHost}' -m command -a '${deployDir}/01-deploy.sh' | tail -1").trim()
            }
        }

    }


    applyDeploy(releaseVersion, activate)
    currentBuild.result = 'SUCCESS'
} catch(err) {
    currentBuild.result = 'FAILURE'
} finally {
    sendMail(mailMessage)
}


def activateNginxConf(activate) {
    node('docker-ansible') {
        def nginxconf = '/etc/nginx/conf.d'
        sh "ansible '${nginxHost}' -m file -a 'state=link src=${nginxconf}/devicehive-server.conf.${activate} dest=${nginxconf}/devicehive-server.conf'"
        sh "ansible '${appHost}' -m command -a 'systemctl reload nginx.service'"
        echo "${nginxconf}/devicehive-server.conf.${activate}"
    }
}


def applyDeploy(latestRelease, activate) {
    try {
        stage('部署确认') {
            def message = "新版本（${latestRelease}）准备就绪，是否部署？"
            input(message, ok: '确定')

        }

        activateNginxConf(activate)
        confirmDeploy(latestRelease)
    } catch(FlowInterruptedException err) {
        rollback()
    }
}

def rollback() {
    try {
        stage('回滚确认') {
            def message = "是否回滚到上一个稳定版本（${stableVersion}）？"
            input(message, ok: '确定')
        }

        node('docker-ansible') {
            stage("回滚到稳定版本（${stableVersion}）") {
                def deployDir = "${projectRoot}"
                activate = sh(returnStdout: true, script: "ansible '${appHost}' -m command -a '${deployDir}/02-rollback.sh' | tail -1").trim()
            }
        }

        activateNginxConf(activate)

        mailMessage = "回滚成功，当前版本：${stableVersion}!"
    } catch(err) {
        mailMessage = "回滚失败!"
        throw err
    }
}

def confirmDeploy(latestRelease) {
    try {
        stage('发布确认') {
            def message = "新版本（${latestRelease}）已经部署，是否发布？"
            input(message, ok: '确定')
        }

        node('docker-ansible') {
            stage("发布新版本（${releaseVersion}）") {
                def releaseDir = "${releaseRoot}/${releaseVersion}"
                def deployDir = "${projectRoot}"
                sh "ansible '${appHost}' -m command -a '${deployDir}/03-deploy-confirm.sh'"
                sh "ansible '${appHost}' -m file -a 'state=link src=${releaseDir} dest=${releaseRoot}/stable'"
            }
        }

        mailMessage = "发布成功，当前版本：${latestRelease}!"
    } catch(FlowInterruptedException err) {
        rollback()
    }
}

def sendMail(message) {
    recipients = 'lvguojian@allwinnertech.com'
    message = "\$DEFAULT_REPLYTO <h3>${message}</h3>"
    emailext attachLog: true,
            body: "${message}",
            replyTo: '$DEFAULT_REPLYTO',
            subject: "${env.MAIL_SUBJECT}",
            to: "${recipients}"
}

def sendConfirmMail(message) {
//    wrap([$class: 'BuildUser']) {
//        def recipients="${env.BUILD_USER_EMAIL}"
//        message = """
//            <br />ReleaseVersion:   ${releaseVersion}
//            <br />DeploymentEnv:    ${deploymentEnv}
//            <a href="${BUILD_URL}console">${message}</a>
//        """
//        emailext body: "${message}", replyTo: '$DEFAULT_REPLYTO', subject: '$DEFAULT_SUBJECT', to: "${recipients}"
//    }
    message = """
            <br />ReleaseVersion:   ${releaseVersion}
            <br />DeploymentEnv:    ${deploymentEnv}
            <a href="${BUILD_URL}console">${message}</a>
        """
    emailext body: "${message}", replyTo: '$DEFAULT_REPLYTO', subject: '$DEFAULT_SUBJECT', to: "lvguojian@allwinnertech.com"
}

