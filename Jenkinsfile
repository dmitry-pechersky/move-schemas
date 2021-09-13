pipeline {
    agent any
    environment {
        EXP_HOST = 'linux02'
        EXP_SERVICE_NAME = 'db01'
        EXP_SCHEMAS = 'SIGMA,DBCCB'
        EXP_CREDENTIALS = credentials('oracle-rdbms-linux02-db01-jenkins-prod-id')
        EXP_DIRECTORY = 'DATA_PUMP_DIR'
        
    }    
    stages {
        stage('Export') {
            steps {
                sh('$PYTHON_INTERPRETER ./python/export_schemas.py')
            }
        }
    }
}
