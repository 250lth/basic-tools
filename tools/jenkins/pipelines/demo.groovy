node {
    git url: 'https://github.com/jglick/simple-maven-project-with-tests.git'
    def mvnHome = tool 'M3'
    env.PATH = "${mvnHome}/bin:${env.PATH}"
    sh 'mvn -B -Dmaven.test.failure.ignore verify'
    input 'save artifacts and unit results?'
    step([$class: 'ArtifactArchiver', artifacts: '**/target/*.jar', fingerprint: true])
    step([$class: 'JUnitResultArchiver', testResults: '**/target/surefire-reports/TEST-*.xml'])
}
