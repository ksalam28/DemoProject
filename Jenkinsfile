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
	      bat 'pip install -r test-requirements.txt'
	      bat 'python test/kubernetes_test.py'
       	      bat 'python test/test.py'
      }
    }
    stage('deploy') {
      steps {
	      bat 'minikube stop'
	      bat 'minikube delete'
      }
    }
  }
}
