pipeline {
    agent {
        docker {
            image 'docker:19.03.13'
            args '-v /var/run/docker.sock:/var/run/docker.sock'
        }
    }
    stages {
        stage('Build') {
            steps {
                sh 'docker build -t saurabh896/sunrise:latest .'
            }
        }
    }
}
