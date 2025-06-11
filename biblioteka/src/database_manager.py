import sqlite3

class DatabaseManager:
    def __init__(self, db_path="data/library.db"):
        self.db_path = db_path

    def connect(self):
        return sqlite3.connect(self.db_path)
