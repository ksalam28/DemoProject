pipeline {
  agent any
  stages {
    stage('build') {
      steps {
	      
	      bat 'C:/Windows/System32/kubectl.exe apply -f elk/elasticsearch'
	      bat 'C:/Windows/System32/kubectl.exe apply -f elk/kibana'
	      bat 'C:/Windows/System32/kubectl.exe apply -f elk/beats_init'
	      bat 'C:/Windows/System32/kubectl.exe apply -f elk/beats_agents'
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
