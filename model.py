import sqlite3 as db

filename = "sqlite.db"

sql_create_budget_table = ''' CREATE TABLE IF NOT EXISTS budget(
                                      transaction_name text NOT NULL,
                                      transaction_type text NOT NULL,
                                      planned_budget integer NOT NULL,
                                      actual_budget integer NOT NULL,
                                      transaction_date text NOT NULL,
                                      update_time text NOT NULL
                                  ); '''
sql_insert_data = ''' INSERT INTO budget VALUES (?,?,?,?,?,?); '''

sql_select_table_data = ''' SELECT * FROM budget; '''


def create_connection(db_file):
    """ create a database connection to the SQLite database
          specified by db_file"""
    conn = None
    try:
        conn = db.connect(db_file)
        return conn
    except Exception as err:
        print(err)
    return conn


def create_table(conn, create_table_sql):
    """ creates a table from the create_table_sql"""
    try:
        crs = conn.cursor()
        crs.execute(create_table_sql)

    except Exception as err:
        print(err)


def initialize_db():
    """ initialize db, if once table created it will not run"""
    conn = create_connection(filename)
    if conn is not None:
        create_table(conn, sql_create_budget_table)
    else:
        print("Error! cannot create the database connection.")
    conn.commit()
