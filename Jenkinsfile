
pipeline{
    agent any
    environment {
        COMPOSE_PROJECT_NAME = "${env.JOB_NAME}-${env.BUILD_ID}"
    }
    stage("1. Checkout"){
        git "https://github.com/hamburger95/WorldOfGames.git"
    }
    stage("2. docker-compose"){
         sh "curl -L https://github/docker/compose/releases/download/1.8.0/docker-compose-`uname -s`-`uname -m` > /usr/local/bin/docker-compose"
    }
}
