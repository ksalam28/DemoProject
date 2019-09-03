pipeline {
  agent any
  stages {
    stage('build') {
      steps {
        bat 'kubectl apply -f elk/elasticsearch'
	bat 'kubectl apply -f elk/kibana'
	bat 'kubectl apply -f elk/beats_init'
	bat 'kubectl apply -f elk/beats_agents'
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
        echo 'Deployed'
      }
    }
  }
}
