pipeline {
  agent { docker { image 'python:3.7.2' } }
  stages {
    stage('build') {
      steps {
        echo '=== install dependency from requirements.txt ==='
        sh 'sudo -H pip install -r requirements.txt'
      }
    }
    stage('test') {
      steps {
        sh 'python test_hello.py'
      }
    }
  }
}