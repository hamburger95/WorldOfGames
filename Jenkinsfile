pipeline {
    agent {docker}
    stages {
        stage('Test') {
            steps {
                sh 'node --version'
                sh 'svn --version'
                sh 'python --version'
            }
        }
    }
}
