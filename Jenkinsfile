pipeline {
    agent any

    // environment {
    // App = 'abracadabra'
    // DOCKERHUB_REGISTRY = 'shaypi'
    // DOCKERHUB_REPOSITORY = 'abracadabra'
    // SHA = "${env.GITHUB_SHA}"
    // DOCKERHUB_CREDENTIALS = credentials('docker')
    // }

    stages {
        stage('Checkout') {
            steps {
                checkout([$class: 'GitSCM',
                          branches: [[name: '*/main']],
                          userRemoteConfigs: [[url: 'https://github.com/shaypi/bluewhite']]])
            }
        }
    //     stage('Install Python 3, pip, and pipenv') {
    //         steps {
    //             sh 'apt-get update'
    //             sh 'apt-get install -y python3 python3-pip'
    //             sh 'pip3 install --user pipenv'
    //             sh 'pip3 install --upgrade Werkzeug'
    //             sh 'pip3 install --upgrade flask werkzeug'
    //         }
    //     }
    //     stage('Install black') {
    //         steps {
    //             sh 'pip install --pre black'
    //         }
    //     }
    //     // stage('Unit Test') {
    //     //     steps {
    //     //         sh 'cd app && python3 -m unittest app.py'
    //     //     }
    //     // }
    //     stage('Build') {
    //         steps {
    //             sh 'cd app && python3 -m pip install -r requirements.txt'
    //         }
    //     }
    //     // stage('Lint') {
    //     //     steps {
    //     //         sh 'black --check .'
    //     //     }
    //     // }
    //     stage('Code Formatting') {
    //         steps {
    //             sh 'black .'
    //         }
    //     }
    //     stage('Docker Login') {
    //         steps {
    //             sh 'echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin'
    //         }
    //     }
    //     stage('Build, tag, and push image to Docker Hub') {
    //         steps {
    //             script {
    //                 sh "docker build -t $App app/"
    //                 sh "docker tag $App $DOCKERHUB_REGISTRY/$DOCKERHUB_REPOSITORY:$SHA"
    //                 sh "docker push $DOCKERHUB_REGISTRY/$DOCKERHUB_REPOSITORY:$SHA"
    //                 sh "docker tag $App $DOCKERHUB_REGISTRY/$DOCKERHUB_REPOSITORY:$App-${env.BUILD_ID}"
    //                 sh "docker push $DOCKERHUB_REGISTRY/$DOCKERHUB_REPOSITORY:$App-${env.BUILD_ID}"
    //             }
    //         }
    //     }
    }
}
