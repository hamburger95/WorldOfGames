node{
    stage("clone"){
        git "https://github.com/hamburger95/WorldOfGames.git"
    }
    stage("build"){
        bat "docker build ."
    }
    stage("run"){
        bat "docker run ."
    }
    stage("exe"){
        bat "pyhton MainScore.py"
    }
}
