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
            }
        }

        stage('Build Docker Image') {
            steps {
                echo "🐳 Building Docker image..."
                sh '''
                    docker build -t aceest_fitness:v6 -f Dockerfile .
                '''
            }
        }

        stage('Run Unit Tests') {
            steps {
                echo "🧪 Running unit tests with pytest..."
                sh '''
                    docker run --rm -v \$(pwd):/app aceest_fitness:v6 sh -c 'pytest -v --maxfail=1 --disable-warnings'
                '''
            }
        }

        stage('Deploy Container') {
            steps {
                echo "🚀 Deploying container..."
                sh '''
                    docker rm -f aceest_fitness_container || true
                    docker run -d --name aceest_fitness_container -p 5001:5000 aceest_fitness:v6
                '''
            }
        }

        stage('Verify Deployment') {
            steps {
                sh 'docker ps'
            }
        }
    }

    post {
        success {
            echo "✅ Build, test, and deploy completed successfully!"
        }
        failure {
            echo "❌ Build failed — check logs for details."
        }
    }
}

