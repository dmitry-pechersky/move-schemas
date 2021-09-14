## In source database
create user jenkins identified by *** default tablespace users;
alter user jenkins quota unlimited on users;
grant DATAPUMP_EXP_FULL_DATABASE to jenkins;
create directory MS_DATA_PUMP_DIR as '/u02/app/oracle/dpdump';
grant all on directory MS_DATA_PUMP_DIR to jenkins;

## In target database:
create user jenkins identified by *** default tablespace users;
grant DATAPUMP_IMP_FULL_DATABASE to jenkins;
alter user jenkins quota unlimited on users;
create directory MS_DATA_PUMP_DIR as '/u02/app/oracle/dpdump';
grant all on directory MS_DATA_PUMP_DIR to jenkins;


