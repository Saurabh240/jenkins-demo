pipeline {
    agent any
    
    environment {
        KUBECONFIG = credentials('kubeconfig-credentials')
    }
    
    stages {
        // stage('Build') {
        //     steps {
        //         // Build Docker image (if needed)
        //     }
        // }
        
        // stage('Test') {
        //     steps {
        //         // Run tests (if needed)
        //     }
        // }
        
        stage('Deploy') {
            steps {
                // Apply Kubernetes manifests
                sh 'kubectl apply -f kubernetes/deployment.yaml'
                sh 'kubectl apply -f kubernetes/service.yaml'
            }
        }
    }
}
