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
                sh 'curl -LO "https://storage.googleapis.com/kubernetes-release/release/v1.20.5/bin/linux/amd64/kubectl"'  
                sh 'chmod u+x ./kubectl'
                sh './kubectl get pods'
                sh './kubectl apply -f kubernetes/deployment.yaml'
                sh './kubectl apply -f kubernetes/service.yaml'
            }
        }
    }
}
