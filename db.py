import pyodbc

DB_HOST = "LAPTOP-IRML9SSB\MSSQLSERVER1"
DB_USER = ""
DB_PASSWORD = ""
DB_NAME = "Hospital"


def get_db_connection():
    try:
        connection_string = (
            f'DRIVER={{SQL Server}};'
            f'SERVER={DB_HOST};'
            f'DATABASE={DB_NAME};'
            f'UID={DB_USER};'
            f'PWD={DB_PASSWORD}'
        )

        conn = pyodbc.connect(connection_string)
        return conn

    except pyodbc.Error as e:
        return None
