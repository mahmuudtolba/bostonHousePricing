pipeline {
  agent any
  stages {
    stage('Checkout code') {
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