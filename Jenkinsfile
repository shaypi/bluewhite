pipeline {
    agent {
        docker {
            image 'ubuntu:20.04'
        }
    }
    stages {
        stage('Checkout') {
            steps {
                checkout([$class: 'GitSCM',
                          branches: [[name: '*/main']],
                          userRemoteConfigs: [[url: 'https://github.com/shaypi/bluewhite']]])
            }
        }
        stage ('Install prerequisites') { 
            steps { 
                sh 'pipenv install --pre --dev black' 
            }
        }
        stage ('Code Formatting') { 
            steps { 
                sh 'pipenv run black .' 
            }
        }
    }
}
