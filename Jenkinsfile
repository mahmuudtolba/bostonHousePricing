pipeline {
  agent any
  stages {
    stage('checkout code') {
      steps {
        git(url: 'https://github.com/mahmuudtolba/bostonHousePricing.git', branch: 'main')
      }
    }

    stage('error') {
      steps {
        sh 'ls -la'
      }
    }

  }
}