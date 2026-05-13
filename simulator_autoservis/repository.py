import sqlite3

class Repository:
    instance = None

    def __init__(self):
        self.db_name = 'auto.db'
        self.connector = sqlite3.connect(self.db_name)
        self.cursor = self.connector.cursor()

    def initialize(self):
        self.create_tables()

    def query(self, sql, params=()):
        return self.connector.execute(sql, params)

    def get_users(self):
        cursor = self.query("SELECT * FROM users")
        return cursor.fetchall()

    def create_tables(self):
        self.connector.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                login TEXT UNIQUE NOT NULL,
                password TEXT NOT NULL
            )
        """)
        self.connector.commit()

    @staticmethod
    def singletone():
        if Repository.instance is None:
            Repository.instance = Repository()

        return Repository.instance

    def get_user_by_login_password(self, login, password):
        cursor = self.query(
            "SELECT * FROM users WHERE login = ? AND password = ?",
            (login, password)
        )
        return cursor.fetchone()

    def close(self):
        self.cursor.close()
        self.connector.close()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()