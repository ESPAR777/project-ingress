pipeline {
agent any

options {
    skipDefaultCheckout()
}

stages {
    stage('Checkout') {
        steps {
            git 'https://github.com/ESPAR777/project-ingress.git'
        }
    }

    stage('Verify Tools') {
        steps {
            sh '''
            echo "Checking tools..."
            docker --version
            python3 --version
            '''
        }
    }

    stage('Build Docker Image') {
        steps {
            sh '''
            docker build -t myapp ./dockerdjango
            '''
        }
    }

    stage('Run App') {
        steps {
            sh '''
            docker stop myapp || true
            docker rm myapp || true
            docker run -d -p 8080:80 --name myapp myapp
            '''
        }
    }
}

}
