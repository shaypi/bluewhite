pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                checkout([$class: 'GitSCM',
                          branches: [[name: '*/main']],
                          userRemoteConfigs: [[url: 'https://github.com/shaypi/bluewhite']]])
            }
        }
        stage('Install Python 3, pip, and pipenv') {
            steps {
                sh 'apt-get update'
                sh 'apt-get install -y python3 python3-pip'
                sh 'pip3 install --user pipenv'
            }
        }
        stage('Install prerequisites') {
            steps {
                sh 'pip install --pre black'
            }
        }
        stage('Code Formatting') {
            steps {
                sh 'pipenv run black .'
            }
        }
    }
}
