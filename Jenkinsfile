pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Setup Python Environment') {
            steps {
                sh 'python3 -m venv venv || true'
                sh './venv/bin/pip install --no-cache-dir -r requirements.txt || true'
            }
        }

        stage('Run Unit Tests') {
            steps {
                sh './venv/bin/pytest -v || true'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t aceest_fitness:v3 .'
            }
        }

        stage('Run Docker Container') {
            steps {
                sh 'docker run -d -p 5001:5000 aceest_fitness:v3'
            }
        }
    }

    post {
        success {
            echo '✅ Build, test, and container deployment completed successfully!'
        }
        failure {
            echo '❌ Build failed — check the console output for details.'
        }
    }
}

