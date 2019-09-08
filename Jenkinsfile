pipeline {
  agent any
  stages {
    stage('build') {
      steps {
	      bat 'minikube start'
	      bat 'kubectl apply -f elk/elasticsearch'
	      bat 'kubectl apply -f elk/kibana'
	      bat 'kubectl apply -f elk/beats_init'
	      bat 'kubectl apply -f elk/beats_agents'
	      bat 'kubectl apply -f app/app-deployment.yml'
      }
    }
    stage('test') {
      steps {
	      bat 'pip install -r test-requirements.txt'
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
