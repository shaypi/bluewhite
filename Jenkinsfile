pipeline {
    agent any

    environment {
        App = 'abracadabra'
        DOCKERHUB_REGISTRY = 'shaypi'
        DOCKERHUB_REPOSITORY = 'abracadabra'
        SHA = "${env.GITHUB_SHA}"
        DOCKERHUB_CREDENTIALS = credentials('docker')
    }

    stages {
        stage('Checkout') {
            steps {
                checkout([$class: 'GitSCM', branches: [[name: '*/main']], userRemoteConfigs: [[url: 'https://github.com/shaypi/bluewhite']]])
            }
        }

        stage('Install Python 3, pip, and pipenv') {
            steps {
                sh 'apt-get update'
                sh 'apt-get install -y python3 python3-pip'
                sh 'pip3 install --user pipenv'
                sh 'pip3 install --upgrade Werkzeug flask'
            }
        }

        stage('Install black') {
            steps {
                sh 'pip3 install --pre black'
            }
        }

        stage('Unit Test') {
            steps {
                sh 'cd app && python3 -m unittest test.py'
            }
        }

        stage('Code Formatting') {
            steps {
                sh 'black .'
            }
        }

        stage('Lint') {
            steps {
                sh 'black --check .'
            }
        }

        stage('Docker Login') {
            steps {
                withCredentials([string(credentialsID: 'docker', variable: 'abracadabra')]) {
                    sh 'echo ${abracadabra} | docker login -u shaypi --password-stdin'
                }
            }
        }
        stage('Build, tag, and push image to Docker Hub') {
            steps {
                script {
                    def imageTag = "$DOCKERHUB_REGISTRY/$DOCKERHUB_REPOSITORY:$SHA"
                    def imageTagWithBuildId = "$DOCKERHUB_REGISTRY/$DOCKERHUB_REPOSITORY:$App-${env.BUILD_ID}"

                    sh "docker build -t $App app/"
                    sh "docker tag $App $imageTag"
                    sh "docker push $imageTag"
                    sh "docker tag $App $imageTagWithBuildId"
                    sh "docker push $imageTagWithBuildId"
                }
            }
        }
    }
}
