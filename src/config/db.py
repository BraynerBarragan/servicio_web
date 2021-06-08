import pyodbc

config = {
    'Driver':'{ODBC Driver 17 for SQL Server}',
    'Server':'DESKTOP-7MMG3L2\SQLEXPRESS',
    'Database':'api_rest',
    'UID':'prueba',
    'PWD':'admin123'
}

DB = pyodbc.connect(**config)
DB.autocommit = True