import pyodbc

class Config:
    DATABASE_CONFIG = {
        'server': 'MSI\\SQLEXPRESS',  
        'database': 'LoginDb',
        'username': 'sa',
        'password': 'Univalle'
    }

    @staticmethod
    def get_db_connection():
        return pyodbc.connect(
            'DRIVER={ODBC Driver 17 for SQL Server};'
            f"SERVER={Config.DATABASE_CONFIG['server']};"
            f"DATABASE={Config.DATABASE_CONFIG['database']};"
            f"UID={Config.DATABASE_CONFIG['username']};"
            f"PWD={Config.DATABASE_CONFIG['password']}"
        )
