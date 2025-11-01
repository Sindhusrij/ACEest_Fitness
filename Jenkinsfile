pipeline {
    agent any

    environment {
        // Ensure Jenkins can access Docker
        PATH = "/opt/homebrew/bin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin"
    }

    stages {

        stage('Checkout') {
            steps {
                echo "📥 Checking out the repository..."
                checkout scm
            }
        }

        stage('Verify Workspace') {
            steps {
                echo "🔍 Checking Jenkins workspace and files..."
                sh 'pwd'
                sh 'ls -la'
                sh 'cat Dockerfile || echo "❌ Dockerfile not found in workspace!"'
            }
        }

        stage('Build Docker Image') {
            steps {
                echo "🛠️ Building Docker image..."
                sh '''
                    docker build -t aceest_fitness:v3 -f Dockerfile . || {
                        echo "❌ Failed to build Docker image — Dockerfile not found or invalid";
                        exit 1;
                    }
                '''
            }
        }

        stage('Run Docker Container') {
            steps {
                echo "🚀 Running Docker container..."
                sh '''
                    # Stop and remove any existing container using the same name
                    docker ps -q --filter "name=aceest_fitness" | xargs -r docker stop
                    docker ps -a -q --filter "name=aceest_fitness" | xargs -r docker rm

                    # Run the new container on port 5001
                    docker run -d -p 5001:5000 --name aceest_fitness aceest_fitness:v3
                '''
            }
        }
    }

    post {
        success {
            echo "✅ Build and container run successful! Visit http://localhost:5001"
        }
        failure {
            echo "❌ Build failed — check console logs for details."
        }
    }
}

