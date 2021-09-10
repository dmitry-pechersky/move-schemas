pipeline {
    agent any
    environment {
       MS_SOURCE_HOST = 'linux02.fly.com'
    }
    stages {
        stage('Hello') {
            steps {
                sh '. ./init.env'
                sh 'python3 ./python/move_schemas.py'
            }
        }
    }
}

