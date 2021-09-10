pipeline {
    agent any
    environment {
       MS_SOURCE_HOST = 'linux02.fly.com'
    }
    stages {
        stage('Hello') {
            steps {
                sh 'python3 ./move_schemas.py'
            }
        }
    }
}

