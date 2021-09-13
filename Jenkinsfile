pipeline {
    agent any
    environment {
        EXP_HOST = 'linux02'
        EXP_SERVICE_NAME = 'db01'
        EXP_SCHEMAS = 'SIGMA'
        EXP_CREDENTIALS = credentials('jenkins-aws-secret-key-id')
    }    
    stages {
        stage('Export') {
            steps {
                sh('python3 ./python/move_schemas.py')
            }
        }
    }
}

