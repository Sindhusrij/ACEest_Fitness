pipeline {
    agent any

    environment {
        PATH = "/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin:/opt/homebrew/bin"
        DOCKER_IMAGE = "sindhujv/aceest_fitness"
        SONARQUBE = credentials('sonar-token')        // Add in Jenkins credentials
        DOCKER_HUB = credentials('docker-hub')        // Add Docker Hub credentials
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
                    docker build -t $DOCKER_IMAGE:latest -t $DOCKER_IMAGE:v6 -f Dockerfile .
                '''
            }
        }

        stage('Run Unit Tests') {
            steps {
                echo "🧪 Running unit tests with pytest..."
                sh '''
                    docker run --rm -v $(pwd):/app $DOCKER_IMAGE:latest sh -c 'pytest -v --maxfail=1 --disable-warnings'
                '''
            }
        }

        stage('Code Quality - SonarQube') {
            steps {
                echo "🔍 Running SonarQube analysis..."
                withSonarQubeEnv('MySonar') {
                    sh '''
                        sonar-scanner \
                            -Dsonar.projectKey=ACEest_Fitness \
                            -Dsonar.sources=. \
                            -Dsonar.host.url=http://localhost:9000 \
                            -Dsonar.login=$SONARQUBE
                    '''
                }
            }
        }

        stage('Push Image to Docker Hub') {
            steps {
                echo "📦 Pushing Docker image to Docker Hub..."
                sh '''
                    echo $DOCKER_HUB_PSW | docker login -u $DOCKER_HUB_USR --password-stdin
                    docker push $DOCKER_IMAGE:latest
                    docker push $DOCKER_IMAGE:v6
                '''
            }
        }

        stage('Deploy Container (Local)') {
            steps {
                echo "🚀 Deploying container locally..."
                sh '''
                    docker rm -f aceest_fitness_container || true
                    docker run -d --name aceest_fitness_container -p 5001:5000 $DOCKER_IMAGE:latest
                '''
            }
        }

        stage('Verify Deployment') {
            steps {
                echo "🔎 Checking running containers..."
                sh 'docker ps'
            }
        }
    }

    post {
        success {
            echo "✅ CI/CD Pipeline executed successfully!"
        }
        failure {
            echo "❌ Pipeline failed. Check logs."
        }
    }
}
