pipeline {
    agent any

    stages {
        stage('Hello') {
            steps {
                sh 'python3 ./move-schemas.py'
            }
        }
    }
}

