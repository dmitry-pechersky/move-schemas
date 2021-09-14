import os
from move_schemas import ODB, rdbms_dp_export

if __name__ == '__main__':
    host = os.environ["EXP_HOST"]
    service_name = os.environ["EXP_SERVICE_NAME"]
    user = os.environ['EXP_CREDENTIALS_USR']
    password = os.environ['EXP_CREDENTIALS_PSW']
    schemas = os.environ['EXP_SCHEMAS']
    directory = os.environ['EXP_DIRECTORY']
    remove_dump_file_if_exist = os.environ.get('EXP_REMOVE_DUMP_FILE_IF_EXIST', default='N')

    if remove_dump_file_if_exist == 'Y':
        db = ODB(host=host, service_name=service_name, user=user, password=password)
        db.remove_dump_files_if_exist(directory, "expdat.dmp")

    rdbms_dp_export(host=host, service_name=service_name, user=user, password=password, schemas=schemas, directory=directory)