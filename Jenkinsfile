pipeline {
    agent {
        docker {
            image 'docker:19.03.13' // Specify the Docker image to use
            args '-v /var/run/docker.sock:/var/run/docker.sock' // Mount Docker socket for Docker inside Docker
        }
    }
    
    stages {
        stage('Checkout') {
            steps {
                // Initialize workspace as Git repository and checkout code
                checkout([$class: 'GitSCM', branches: [[name: 'main']], userRemoteConfigs: [[url: 'https://github.com/Saurabh240/sunrise.git']]])
            }
        }
        stage('Build Docker Image') {
            steps {
                // Build Docker image
                script {
                    docker.build('saurabh896/sunrise:latest')
                }
            }
        }
        stage('Run Tests') {
            steps {
                // Run tests inside Docker container
                script {
                    docker.image('saurabh896/sunrise:latest').inside {
                        sh 'python -m unittest discover tests'
                    }
                }
            }
        }
        stage('Generate Artifacts') {
            steps {
                // Generate artifacts (e.g., Docker image)
                script {
                    docker.image('saurabh896/sunrise:latest').push('https://registry.hub.docker.com/saurabh896/sunrise:latest')
                }
            }
        }
    }
    post {
        success {
            // Trigger deployment stage if build and tests are successful
            echo 'Build succeeded! Triggering deployment...'
            // You can trigger deployment stage here
        }
    }
}
