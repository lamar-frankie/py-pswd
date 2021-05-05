pipeline {
  agent any
  stages {
    stage('Test') {
      steps {
        sh '''pip install -r requirements.txt
pytest -xv test_passwd.py'''
      }
    }

  }
}