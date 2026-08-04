pipeline {
    agent any

    stages {

        stage('Checkout Code') {
            steps {
                git 'https://github.com/ESPAR777/project-ingress.git'
            }
        }

        stage('List Files') {
            steps {
                sh 'ls -l'
            }
        }

        stage('Build Step') {
            steps {
                echo 'Build stage running...'
            }
        }

        stage('Test Step') {
            steps {
                echo 'Test stage running...'
            }
        }

        stage('Deploy Step') {
            steps {
                echo 'Deploy stage running...'
            }
        }
    }
}
