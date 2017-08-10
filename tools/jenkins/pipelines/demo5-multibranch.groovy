https://github.com/ciandcd/example_jenkins_multibranch/blob/b1/Jenkinsfile
https://github.com/ciandcd/example_jenkins_multibranch/blob/master/Jenkinsfile

node () {
	stage 'Build and Test'
	env.PATH = "${tool 'M3'}/bin:${env.PATH}"
	checkout scm
	sh 'mvn clean package'
}
