pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo '📥 Checking out source code...'
                checkout scm
                sh 'pwd'
                sh 'ls -la'
            }
        }

        stage('Build Docker Image') {
            steps {
                echo '✅ Building Docker image...'
                sh '''
                    echo "Current directory: $(pwd)"
                    echo "Files:"
                    ls -la
                    docker build -t aceest_fitness:v3 -f Dockerfile .
                '''
            }
        }

        stage('Run Docker Container') {
            steps {
                echo '🚀 Running container...'
                sh '''
                    docker run -d -p 5001:5000 aceest_fitness:v3
                    docker ps
                '''
            }
        }
    }

    post {
        success {
            echo '🎉 Build and container run successful!'
        }
        failure {
            echo '❌ Build failed — check the logs.'
        }
    }
}

