pipeline{
    agent any
    environment {
        COMPOSE_PROJECT_NAME = "${env.JOB_NAME}-${env.BUILD_ID}"
    }
    stage("1. Checkout"){
        git "https://github.com/hamburger95/WorldOfGames.git"
    }
}
