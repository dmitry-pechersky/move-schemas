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
                sh('$PYTHON_INTERPRETER ./python/export_schemas.py ${EXP_CREDENTIALS_USR} ${EXP_CREDENTIALS_PSW}')
            }
        }
    }
}

