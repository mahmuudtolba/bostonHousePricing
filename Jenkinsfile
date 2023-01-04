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

  }
}