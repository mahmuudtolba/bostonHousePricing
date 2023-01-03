pipeline {
  agent any
  stages {
    stage('Checkout Code') {
      steps {
        git(url: 'https://github.com/mahmuudtolba/bostonHousePricing.git', branch: 'main')
        sh 'ls -la'
      }
    }

    stage('Build') {
      steps {
        sh 'docker build -f mahmuudtolba/houseprice .'
      }
    }

    stage('login ') {
      environment {
        DOCKERHUB_USER = 'mahmuudtolba'
        DOCKERHUB_PASSWORD = 'Mahmud132465'
      }
      steps {
        sh 'docker login -u $DOCKERHUB_USER -P $DOCKERHUB_PASSWORD'
      }
    }

    stage('PUSH') {
      steps {
        sh 'docker push mahmuudtolba/houseprice:latest'
      }
    }

  }
}