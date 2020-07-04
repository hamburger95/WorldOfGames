node{
    stage("1. Checkout"){
        git "https://github.com/hamburger95/WorldOfGames.git"
    }
    stage("2. docker-compose"){
        sh label: '', script: 'docker-compose up'
    }
}
