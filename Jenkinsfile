pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
               script {
                    docker.build
               }
           }
        }
        stage('Test') {
            steps {
                echo 'Testing..'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
            }
        }
    }
}
