pipeline {
    agent any

    stages {
        stage('Code') {
            steps {
                git url: 'https://github.com/srahul0502/Demo.git',branch:'master'
                echo 'Code Cloned'
            }
        }
        stage('Build Image') {
            steps {
                sh 'docker build -t flask-app .'
                echo 'Image built'
            }
        }
        stage('Run Docker Container') {
            steps {
                sh 'docker run -d -p 5000:5000 flask-app:latest'
                echo 'Container is up and running'
            }
        }
    }
}

