pipeline {
agent any

stages {
    stage('Hello') {
        steps {
            echo 'Hello CI/CD'
        }
    }

    stage('Checkout') {
        steps {
            git 'https://github.com/ESPAR777/project-ingress.git'
            sh 'ls -l'
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
