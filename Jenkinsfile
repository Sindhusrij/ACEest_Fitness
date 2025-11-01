pipeline {
    agent any

    environment {
        PATH = "/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin:/opt/homebrew/bin"
    }

    stages {

        stage('Checkout') {
            steps {
                echo "📥 Checking out source code..."
                checkout scm
                sh '''
                    echo "Current workspace:"
                    pwd
                    echo "Files in workspace:"
                    ls -la
                '''
            }
        }

        stage('Build Docker Image') {
            steps {
                echo "🐳 Building Docker image..."
                sh '''
                    echo "Using Docker path: $(which docker)"
                    docker --version
                    docker build -t aceest_fitness:v3 -f Dockerfile .
                '''
            }
        }

        stage('Run Docker Container') {
            steps {
                echo "🚀 Running container..."
                sh '''
                    docker ps -a
                    echo "Cleaning up old containers if any..."
                    docker rm -f aceest_fitness_container || true
                    echo "Starting new container..."
                    docker run -d --name aceest_fitness_container -p 5001:5000 aceest_fitness:v3
                '''
            }
        }

        stage('Verify Deployment') {
            steps {
                echo "🔍 Checking running containers..."
                sh 'docker ps'
            }
        }
    }

    post {
        success {
            echo "✅ Build and deployment successful!"
        }
        failure {
            echo "❌ Build failed — check the logs."
        }
    }
}

