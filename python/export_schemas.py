import os
import cx_Oracle
import sys
import subprocess
import time

class MSException(Exception):
    pass

class ODB:
    def __init__(self, host, service_name, user, password):
        dsn = f"{host}/{service_name}"
        self.connection = cx_Oracle.connect(user=user, password=password, dsn=dsn)

    def user_exists(self, user):
        with self.connection.cursor() as cursor:
            res_set = cursor.execute("select count(*) cnt from dba_users where username = :user_name", user_name=user).fetchone()
            return res_set[0] == 1

def rdbms_export(host, service_name, user, password, schemas, directory):
    subprocess.run(["expdp", f'{user}@"{host}/{service_name}"', f"SCHEMAS={schemas}", "COMPRESSION=ALL", f"DIRECTORY={directory}"],
                   check=True, text=True, 
                   input=f"{password}\n")

if __name__ == '__main__':
    exp_host = os.environ["EXP_HOST"]
    exp_service_name = os.environ["EXP_SERVICE_NAME"]
    exp_user = os.environ['EXP_CREDENTIALS_USR']
    exp_password = os.environ['EXP_CREDENTIALS_PSW']
    exp_schemas = os.environ['EXP_SCHEMAS']
    exp_directory = os.environ['EXP_DIRECTORY']

    """
    source_db = ODB(host=os.environ["EXP_HOST"], 
                    service_name=os.environ["EXP_SERVICE_NAME"], 
                    user=os.environ['EXP_CREDENTIALS_USR'], 
                    password=os.environ['EXP_CREDENTIALS_PSW'])
    if not source_db.user_exists(schema):
        raise MSException(f"User {schema} doesn't exist")
    """
    rdbms_export(host=exp_host, service_name=exp_service_name, user=exp_user, password=exp_password, 
                 schemas=exp_schemas, directory=exp_directory)