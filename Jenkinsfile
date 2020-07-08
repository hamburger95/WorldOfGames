pipeline {
    agent { dockerfile true }
    stages {
        stage('Test') {
            steps {
                docker.build("runtestdevops/node")
            }
        }
    }
}
