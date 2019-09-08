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
	      bat 'kubect apply -f app/app-deployment.yml'
      }
    }
    stage('test') {
      steps {
       		bat 'python test.py'
      }
      post {
        always {
          junit 'test-reports/*.xml'
        }
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
