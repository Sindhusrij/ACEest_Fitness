pipeline {
    agent any

    environment {
        DOCKER_PATH = '/opt/homebrew/bin/docker'
        WORKSPACE_DIR = '/Users/sindhujv/.jenkins/workspace/ACEest_Fitness_CI'
    }

    stages {
        stage('Checkout') {
            steps {
                echo '📥 Checking out source code...'
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
                echo '🐳 Building Docker image...'
                sh '''
                    echo "Using Docker path: $DOCKER_PATH"
                    echo "Building from workspace: $WORKSPACE_DIR"
                    $DOCKER_PATH build -t aceest_fitness:v3 -f $WORKSPACE_DIR/Dockerfile $WORKSPACE_DIR
                '''
            }
        }

        stage('Run Docker Container') {
            steps {
                echo '🚀 Running container...'
                sh '''
                    $DOCKER_PATH run -d -p 5001:5000 aceest_fitness:v3
                    $DOCKER_PATH ps
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

