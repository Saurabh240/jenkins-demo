pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                // Initialize workspace as Git repository and checkout code
                checkout([$class: 'GitSCM', branches: [[name: 'main']], userRemoteConfigs: [[url: 'https://github.com/roeeelnekave/sunrise.git']]])
            }
        }
        stage('Build Docker Image') {
            steps {
                // Build Docker image
                script {
                    docker.build('roeeel/sunrise:latest')
                }
            }
        }
        stage('Run Tests') {
            steps {
                // Run tests inside Docker container
                script {
                    docker.image('roeeel/sunrise:latest').inside {
                        sh 'python -m unittest discover tests'
                    }
                }
            }
        }
        stage('Generate Artifacts') {
            steps {
                // Generate artifacts (e.g., Docker image)
                script {
                    docker.image('roeeel/sunrise:latest').push('https://registry.hub.docker.com/roeeel/sunrise:latest')
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
