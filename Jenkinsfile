pipeline {
  agent any
  stages {
    stage('build') {
      steps {
        sh 'kubectl apply -f elk/elasticsearch'
		sh 'kubectl apply -f elk/kibana'
		sh 'kubectl apply -f elk/beats_init'
		sh 'kubectl apply -f elk/beats_agents'
      }
    }
    stage('test') {
      steps {
        sh 'python test.py'
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