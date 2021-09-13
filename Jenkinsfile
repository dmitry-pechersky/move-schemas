pipeline {
    agent any
    environment {
        EXP_HOST = 'linux02'
        EXP_SERVICE_NAME = 'db01'
        EXP_SCHEMAS = 'SIGMA'
        EXP_CREDENTIALS = credentials('oracle-rdbms-linux02-db01-jenkins-prod-id')
    }    
    stages {
        stage('Export') {
            steps {
                sh '. ~/venv/bin/activate'
                sh('python3 ./python/export_schemas.py')
            }
        }
    }
}

