pipeline {
    agent {
        docker {
            image 'ubuntu:20.04'
        }
    }
    stages {
        stage ('Checkout') {
            steps {
                checkout scm
            }
        }
        stage ('Install prerequisites') { 
            steps { 
                sh 'pipenv install --pre --dev black' 
            }
        }
        stage ('Code Formatting') { 
            steps { 
                echo 'Running build phase.' 
            }
        }
        stage ('Lint') { 
            steps { 
                echo 'Running build phase.' 
            }
        }
        stage ('Sonarqube') { 
            steps { 
                echo 'Running build phase.' 
            }
        }
        stage ('Build') { 
            steps { 
                echo 'Running build phase.' 
            }
        }
        stage ('UnitTest') { 
            steps { 
                echo 'Running build phase.' 
            }    
        }
        stage ('Build Image') { 
            steps { 
                echo 'Running build phase.' 
            }
        }
        stage ('Container Validation') { 
            steps { 
                echo 'Running build phase.' 
            }
        }
    }
}
