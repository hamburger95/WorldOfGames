node{
    stage("1. Checkout"){
        git "https://github.com/hamburger95/WorldOfGames.git"
    }
    stage("2. Build container from image"){
        Docker build .
    }
    stage("3. Run container"){
        Docker run .
    }
    stage("4. Test our web service with e2e.py."){
        bat 'python e2e.py'
    }
    stage("5. Finalize"){
        bat 'sudo docker ps'
    }
}
