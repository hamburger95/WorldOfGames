pipeline {
    agent any
    stages {
        stage('Checkout git repo') {
            steps {
                sh 'echo "step 1: Checkout git repo"'
                sh 'git clone https://github.com/hamburger95/WorldOfGames.git'
            }
        }
        stage('Build') {
            steps {
                sh 'echo "step 2: build docker ."'
                sh  'docker build .'
            }
        }
                stage('Run') {
            steps {
                sh 'echo "step 3: run docker ."'
                sh 'sh IMAGE_ID=$(sudo docker images --filter=reference=image_name --format "{{.ID}}"'
                sh  'docker run -p 5000:5000 $IMAGE_ID'
            }
        }

    }
}