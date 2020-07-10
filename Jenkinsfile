pipeline {
    agent any
    stages {
        stage('1. Checkout') {
            steps {
                sh 'echo "step 1: Checkout git repo"'
                checkout scm
            }
        }
        stage('2. Build') {
            steps {
                sh 'echo "step 2: build docker "'
                sh  'docker build .'
            }
        }
        stage('3. Run') {
            steps {
                sh 'echo "step 3: run docker "'
                sh '''docker run -p 5000:5000 -t $(docker images | awk '{print $3}' | awk 'NR==2')'''
                sh '''docker exec -it $(docker images | awk '{print $3}' | awk 'NR==2') sh pwd'''
                sh 'pwd'
            }
        }
        stage('4. Test') {
            steps {
                sh 'python e2e.py'

            }
        }

    }
}