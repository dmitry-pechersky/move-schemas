pipeline {
    agent any
    environment {
        EXP_HOST = 'linux02'
        EXP_SERVICE_NAME = 'db01'
        EXP_SCHEMAS = 'SIGMA,DBCCB'
        EXP_CREDENTIALS = credentials('oracle-rdbms-linux02-db01-jenkins-prod-id')
        EXP_DIRECTORY = 'MS_DATA_PUMP_DIR'
        EXP_REMOVE_DUMP_FILE_IF_EXIST = 'Y'
        IMP_HOST = 'linux02'
        IMP_SERVICE_NAME = 'db02'
        IMP_SCHEMAS = 'SIGMA,DBCCB'
        IMP_CREDENTIALS = credentials('oracle-rdbms-linux02-db02-jenkins-test-id')
        IMP_DIRECTORY = 'MS_DATA_PUMP_DIR'
        IMP_DROP_SCHEMA_IF_EXIST = 'Y'
    }    
    stages {
        stage('Export') {
            steps {
                sh('$PYTHON_INTERPRETER ./python/export_schemas.py')
            }
        }
        stage('Import') {
            steps {
                sh('$PYTHON_INTERPRETER ./python/import_schemas.py')
            }
        }
    }
}
