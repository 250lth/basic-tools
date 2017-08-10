node {
	git url: 'https://github.com/jglick/simple-maven-project-with-tests.git'
	def v = version(readFile('pom.xml'))
	if (v) {
		echo "Building version ${v}"
	}
	def mvnHome = tool 'M3'
	sh "${mvnHome}/bin/mvn -B -Dmaven.test.failure.ignore verify"
	step([$class: 'ArtifactArchiver', artifacts: '**/target/*.jar', fingerprint: true])
	step([$class: 'JUnitResultArchiver', testResults: '**/target/surefire-reports/TEST-*.xml'])
}

@NonCPS
def version(text) {
	def matcher = text =~ '<version>(.+)</version>'
	matcher ? matcher[0][1] : null
}
