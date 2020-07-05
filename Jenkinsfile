pipeline {
    agent { dockerfile true }
    stages {
        stage('Test') {
            steps {
                sh 'pwd'
                sh 'ls'
                sh 'cat Jenkinsfile'
            }
        }
    }
}
