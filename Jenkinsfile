pipeline {
    agent any
    stages {
        stage('1. Checkout') {
            steps {
                sh 'echo "step 1: Checkout git repo.."'
                checkout scm
            }
        }
        stage('2. Build') {
            steps {
                sh 'echo "step 2: build docker .."'
                sh 'docker stop $(docker ps -a -q)'
                sh 'docker rm $(docker ps -a -q)'
                sh 'docker build -t docker-image .'
            }
        }
        stage('3. Run') {
            steps {
                sh 'echo "step 3: run docker .."'
                sh '''docker run --mount type=bind,source=$(pwd)/Scores.txt,target=/code/Scores.txt -d --name docker-app -p 5000:5000 -t $(docker images | awk '{print $3}' | awk 'NR==2')'''
            }
        }
        stage('4. Test ..') {
            steps {
                sh 'docker ps'
                sh 'docker exec docker-app pwd'
                sh 'docker exec docker-app python e2e.py'
            }
        }
        stage('5. Push image to dockerhub ..') {
            steps {
                sh 'docker ps'
                sh 'docker login'
                sh 'docker commit docker-app docker-image:latest'
                sh 'docker tag docker-image:latest idodockerhub/docker-image:latest'
                sh 'docker push idodockerhub/docker-image:latest'
                sh 'docker stop $(docker ps -a -q)'
                sh 'docker rm $(docker ps -a -q)'
                sh 'docker ps'
            }
        }

    }
}