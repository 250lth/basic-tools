properties([
        parameters([
                string(defaultValue: '', name: 'GitCommitId', description: 'git commit id, default is HEAD')
        ])
])

gitlabHost = '192.168.10.11'
gitlabCredential = 'gitlab-jetty-key'
gitCommitId  = "${params.GitCommitId}"

def updateConfig(gitCommitId, objectsUpdate, workspace, gitProject, deployEnv, activate) {
    dir(gitProject) {
        git branch: 'master', credentialsId: "${gitlabCredential}", url: "git@${gitlabHost}:springcloud/${gitProject}.git"
        echo "###### sync config file to ${gitProject} ######"
        objectsUpdate.eachWithIndex { obj, idx ->
            if (obj.deployEnv != deployEnv) {
                return
            }

            echo "# ${idx}. ${obj.configFile}"
            def configFile
            if (obj.projectName == 'event-engine' || obj.projectName == 'mqtt-broker') {
                configFile = "cloud-config/${obj.projectName}/${activate}/${obj.configFileName}"
            } else {
                configFile = "cloud-config/${obj.projectName}-${activate}.txt"
            }

            def exists = fileExists(configFile)
            sh "rm -f ${configFile}"
            sh "cp ${workspace}/profile/${obj.configFile} ${workspace}/${gitProject}/${configFile}"
            if (!exists) {
                sh "git add ${configFile}"
            }
        }

        sshagent(credentials: [gitlabCredential]) {
            sh "git config user.email 'mmzhcn@163.com'"
            sh "git config user.name 'jetty'"
            sh "git status"
            sh "git diff-index --quiet HEAD || git commit -a -m 'sync bbc/profile commit: ${gitCommitId}'"
            sh "git push origin master"
        }

        echo "###### sync successfully ######"
    }
}

node {

    try {
        def workspace = pwd()
        def objectsUpdate = []

        deleteDir()

        stage('collect commit files') {
            dir('profile') {
                git branch: 'master', credentialsId: "${gitlabCredential}", url: "git@${gitlabHost}:bbc/profile.git"
                if (gitCommitId == '') {
                    gitCommitId = sh(returnStdout: true, script: 'git rev-parse HEAD').trim()
                }

                def filesCommit = sh(returnStdout: true, script: "git diff-tree --no-commit-id --name-only -r ${gitCommitId} | xargs").split()
                def regexps = [/^(event\-engine)\/(\w+)\/(.+)$/,
                               /^(mqtt\-broker)\/(\w+)\/(.+)$/,
                               /^(\w+)\/(\w+)\/(application.properties)$/,
                               /^(\w+)\/(\w+)\/(config.js)$/,
                               /^(\w+)\/(\w+)\/\w+\/(settings.py)$/]
                filesCommit.each {f ->
                    echo "${f}"

                    regexps.each { r ->
                        def m = (f =~ r)
                        if (!m) {
                            return
                        }

                        def projectName = m.group(1)
                        def deployEnv = m.group(2)
                        def configFileName = m.group(3)
                        objectsUpdate.add([projectName: projectName, deployEnv: deployEnv, configFile: f, configFileName: configFileName])
                    }
                }
            }
        }



        stage('sync test configserver') {
            def gitProject = 'spring-cloud-config-devtest'
            def deployEnv = 'test'
            def activate = 'qa'
            updateConfig(gitCommitId, objectsUpdate, workspace, gitProject, deployEnv, activate)
        }

        stage('sync prod configserver') {
            def gitProject = 'spring-cloud-config'
            def deployEnv = 'prod'
            def activate = 'prod'
            updateConfig(gitCommitId, objectsUpdate, workspace, gitProject, deployEnv, activate)
        }

        currentBuild.result = 'SUCCESS'
    } catch (err) {
        currentBuild.result = 'FAILURE'
        throw err
    } finally {
        emailext attachLog: true,
                body: '$DEFAULT_CONTENT',
                replyTo: '$DEFAULT_REPLYTO',
                subject: '$DEFAULT_SUBJECT',
                to: '$DEFAULT_RECIPIENTS'
    }

}%   
