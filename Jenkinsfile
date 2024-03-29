pipeline {
    agent any

    environment {
        App = 'abracadabra'
        DOCKERHUB_REGISTRY = 'shaypi'
        DOCKERHUB_REPOSITORY = 'abracadabra'
        DOCKERHUB_CREDENTIALS = credentials('docker')
    }

    options {
        disableConcurrentBuilds()
        skipDefaultCheckout()
        timestamps()
    }

    triggers {
        GenericTrigger(
                genericVariables: [
                        [key: 'Commit_id', value: '$.pull_request.head.sha', defaultValue: 'None'],
                        [key: 'PR_number', value: '$.number', defaultValue: 'None'],
                        [key: 'Repository', value: '$.pull_request.base.repo.full_name', defaultValue: 'None'],
                        [key: 'User', value: '$.pull_request.user.login', defaultValue: 'None'],
                        [key: 'action', value: '$.action', defaultValue: 'None'],
                ],

                causeString: 'Triggered on $PR_number',
                token: 'abra',
                printContributedVariables: true,
                printPostContent: true,
                silentResponse: false,
                regexpFilterText: '$action',
                regexpFilterExpression: '(opened|reopened|synchronize)'
        )
    }


    stages {
        stage('Checkout') {
            steps {
                checkout([$class: 'GitSCM', branches: [[name: '*/main']], userRemoteConfigs: [[url: 'https://github.com/shaypi/bluewhite']]])
            }
        }

        stage('Install Python 3, pip, and pipenv') {
            steps {
                script {
                sh '''
                    apt-get update && \
                    apt-get install -y python3 python3-pip && \
                    pip3 install --user pipenv && \
                    pip3 install Werkzeug flask && \
                    pip3 install --pre black
                '''
                }
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

        stage('Docker login') {
            steps {
                sh 'echo $DOCKERHUB_CREDENTIALS | docker login -u shaypi --password-stdin'
                echo 'Login Completed'
            }
        }

        stage('Build, tag, and push image to Docker Hub') {
            steps {
                script {
                    def imageTagWithBuildId = "$DOCKERHUB_REGISTRY/$DOCKERHUB_REPOSITORY:$App-${env.BUILD_ID}"

                    sh "docker build -t $App app/"
                    sh "docker tag $App $imageTagWithBuildId"
                    sh "docker push $imageTagWithBuildId"
                }
            }
        }

        stage('Test Container') {
            steps {
                sh "docker run $DOCKERHUB_REGISTRY/$DOCKERHUB_REPOSITORY:$App-${env.BUILD_ID} python3 -m unittest test.py"
            }
        }
    }
}
