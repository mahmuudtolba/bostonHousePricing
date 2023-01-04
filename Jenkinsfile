pipeline {
  agent any
  stages {
    stage('Checkout Code') {
      steps {
        git(url: 'https://github.com/mahmuudtolba/autoencoder.git', branch: 'main')
      }
    }

    stage('Build') {
      steps {
        sh 'docker build -t mahmuudtolba/jenkins_docker . '
      }
    }

    stage('Log in Docker') {
      environment {
        DOCKERHUB_USER = 'mahmuudtolba'
        DOCKERHUB_PASSWORD = 'Mahmud132465'
      }
      steps {
        sh 'docker login -u $DOCKERHUB_USER -p $DOCKERHUB_PASSWORD'
      }
    }

    stage('push') {
      steps {
        sh 'docker push mahmuudtolba/jenkins_docker'
      }
    }

  }
}