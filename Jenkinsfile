pipeline {
    agent any
    stages {
        stage('Checkout git repo') {
            steps {
                sh 'echo "step 1: Checkout git repo"'
                checkout scm
            }
        }
        stage('Build') {
            steps {
                sh 'echo "step 2: build docker "'
                sh  'docker build .'
            }
        }
                stage('Run') {
            steps {
                sh 'echo "step 3: run docker "'
                sh '''IMAGE_ID=$(docker images | awk '{print $3}' | awk 'NR==2')'''
                sh 'docker run -p 5000:5000 -t $IMAGE_ID'
            }
        }

    }
}