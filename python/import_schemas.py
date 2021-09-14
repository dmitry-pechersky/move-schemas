import os
from move_schemas import ODB, rdbms_dp_import

if __name__ == '__main__':
    host = os.environ["IMP_HOST"]
    service_name = os.environ["IMP_SERVICE_NAME"]
    user = os.environ['IMP_CREDENTIALS_USR']
    password = os.environ['IMP_CREDENTIALS_PSW']
    schemas = os.environ['IMP_SCHEMAS']
    directory = os.environ['IMP_DIRECTORY']
    drop_schema_if_exist = os.environ.get('IMP_DROP_SCHEMA_IF_EXIST', default='N')

    if drop_schema_if_exist == 'Y':
        db = ODB(host=host, service_name=service_name, user=user, password=password)
        for schema in schemas.split(','):
            db.drop_user_if_exist(schema)

    rdbms_dp_import(host=host, service_name=service_name, user=user, password=password, schemas=schemas, directory=directory)