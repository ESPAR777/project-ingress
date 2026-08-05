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
}

}
