node() {
	stage 'Build and Test'
	env.PATH = "${tool 'M3'}/bin:${env.PATH}"
	//checkout scm
	git url: "https://github.com/ciandcd/simple-maven-project-with-tests.git"
	sh 'mvn clean package"
}
