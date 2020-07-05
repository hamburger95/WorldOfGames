pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
               script {
                    docker.build registry + ":$BUILD_NUMBER"
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
