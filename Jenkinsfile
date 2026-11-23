
pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/enhacfe/devops-assignment3.git'
            }
        }

        stage('Package') {
            steps {
                sh 'docker build -t assignment3-web .'
                sh 'docker build -t assignment3-tests ./tests'
            }
        }

        stage('Start') {
            steps {
                sh 'docker network inspect assignment3-net >/dev/null 2>&1 || docker network create assignment3-net'
                sh 'docker rm -f assignment3-test-web || true'
                sh 'docker run -d --name assignment3-test-web --network assignment3-net --network-alias web assignment3-web'
            }
        }

        stage('Test') {
            steps {
                sh 'docker run --rm --network assignment3-net -e BASE_URL=http://web assignment3-tests'
            }
        }

        stage('Deploy') {
            steps {
                sh 'docker rm -f assignment3-deployed || true'
                sh 'docker run -d --name assignment3-deployed -p 8082:80 assignment3-web'
            }
        }
    }

    post {
        always {
            sh 'docker rm -f assignment3-test-web || true'
        }
    }
}
