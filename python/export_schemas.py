import os
import cx_Oracle
import sys

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

if __name__ == '__main__':
    for i in os.environ['EXP_CREDENTIALS_USR']:
        print("C" + i)
    for i in os.environ['EXP_CREDENTIALS_PSW']:
        print("C" + i)
    """
    source_db = ODB(host=os.environ["MS_SOURCE_HOST"], service_name=os.environ["MS_SOURCE_SERVICE_NAME"], user='jenkins', password='hdd8d83ddef34')
    """
    source_db = ODB(host=os.environ["EXP_HOST"], 
                    service_name=os.environ["EXP_SERVICE_NAME"], 
                    user=os.environ['EXP_CREDENTIALS_USR'], 
                    password=os.environ['EXP_CREDENTIALS_PSW'])
    """

    if not source_db.user_exists(schema):
        raise MSException(f"User {schema} doesn't exist")
    """