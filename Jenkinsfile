pipeline {
  agent any
  stages {
    stage('build') {
      steps {
	      bat 'python build.py'
      }
    }
    stage('test') {
      steps {
       	      bat 'python test.py'
      }
    }
    stage('deploy') {
      steps {
	      bat 'python deploy.py'
      }
    }
  }
}
