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
                sh '''docker run --mount type=bind,source=$(pwd)/Scores.txt,target=/code/Scores.txt -d -p 5000:5000 -t $(docker images | awk '{print $3}' | awk 'NR==2')'''
            }
        }
        stage('4. Test') {
            steps {
                sh 'echo docker ps --format "{{.Names}}"'
                sh 'python3 e2e.py'
            }
        }

    }
}