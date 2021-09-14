import cx_Oracle
import subprocess

class ODB:
    def __init__(self, host, service_name, user, password):
        dsn = f"{host}/{service_name}"
        self.connection = cx_Oracle.connect(user=user, password=password, dsn=dsn)

    def _user_exist(self, user):
        with self.connection.cursor() as cursor:
            res_set = cursor.execute("select count(*) cnt from dba_users where username = :user_name", user_name=user).fetchone()
            return res_set[0] == 1

    def _drop_user(self, user):
        with self.connection.cursor() as cursor:
            res_set = cursor.execute(f"drop user {user} cascade")

    def drop_user_if_exist(self, user):
        if self._user_exist(user):
            self._drop_user(user)

    def _file_exist(self, directory, file_name):
        with self.connection.cursor() as cursor:
            fexists = cursor.var(bool)
            file_length = cursor.var(int)
            block_size = cursor.var(int)
            cursor.callproc("utl_file.fgetattr", [directory, file_name, fexists, file_length, block_size])
            return fexists.getvalue()

    def _remove_file(self, directory, file_name):
        with self.connection.cursor() as cursor:
            cursor.callproc("utl_file.fremove", [directory, file_name])

    def remove_dump_files_if_exist(self, directory, file_name):
        if self._file_exist(directory, file_name):
            self._remove_file(directory, file_name)

def rdbms_dp_export(host, service_name, user, password, schemas, directory):
    subprocess.run(["expdp", f'{user}@"{host}/{service_name}"', f"SCHEMAS={schemas}", "COMPRESSION=ALL", f"DIRECTORY={directory}"],
                   check=True, encoding='utf-8', 
                   input=f"{password}\n")

def rdbms_dp_import(host, service_name, user, password, schemas, directory):
    subprocess.run(["impdp", f'{user}@"{host}/{service_name}"', f"SCHEMAS={schemas}", f"DIRECTORY={directory}"],
                   check=True, encoding='utf-8', 
                   input=f"{password}\n")
