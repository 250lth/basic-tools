node {
	git url: 'https://github.com/jenkinsci/parallel-test-executor-plugin-sample.git'
	archive 'pom.xml, src/'
}

def splits = splitTests([$class: 'CountDrivenParallelism', size: 2])
def branches = [:]
for (int i = 0; i < splits.size(); i++) {
	def exclusions = splits.get(i)
	branches["split${i}"] = {
		node {
			sh 'rm -rf *'
			unarchive mapping: ['pom.xml': '.', 'src/': '.']
			writeFile file: 'exclusions.txt', text: exclusions.join("\n")
			sh "${tool 'M3'}/bin/mvn -B -Dmaven.test.failure.ignore test"
			step([$class: 'JUnitResultArchiver', testResults: 'target/surefire-reports/*.xml'])
		}
	}
}

parallel branches 
