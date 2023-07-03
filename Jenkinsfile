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
                sh 'pip3 install --upgrade Werkzeug'
                sh 'pip3 install --upgrade flask werkzeug'
            }
        }
        stage('Install black') {
            steps {
                sh 'pip install --pre black'
            }
        }
        // stage('Unit Test') {
        //     steps {
        //         sh 'cd app && python3 -m unittest app.py'
        //     }
        // }
        stage('Build') {
            steps {
                sh 'cd app && python3 -m pip install -r requirements.txt'
            }
        }
        // stage('Lint') {
        //     steps {
        //         sh 'black --check .'
        //     }
        // }
        stage('Code Formatting') {
            steps {
                sh 'black .'
            }
        }
    }
}
