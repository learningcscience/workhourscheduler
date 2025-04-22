import sqlite3

class DatabaseManager:
    
    _instance = None
    
    def __init__(self, db_file="work_hours.db"):
        self.conn = sqlite3.connect(db_file)
        self.conn.row_factory = sqlite3.Row
        self.cur = self.conn.cursor()


    @classmethod
    def get_instance(cls):
        if not cls._instance:
            cls._instance = DatabaseManager()

        return cls._instance                 


    def execute(self, query, params=()):
        self.cur.execute(query, params)
        self.conn.commit()
        return self.cur


    def fetchall(self):
        return self.cur.fetchall()


