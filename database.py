import sqlite3
from datetime import datetime

class DatabaseManager:
    def __init__(self, db_name="tips_history.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self._create_table()

    def _create_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS calculations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            bill_amount REAL NOT NULL,
            tax_percent REAL NOT NULL,
            tip_percent REAL NOT NULL,
            people_count INTEGER NOT NULL,
            total_sum REAL NOT NULL,
            per_person REAL NOT NULL,
            created_at TEXT NOT NULL
        );
        """
        self.cursor.execute(query)
        self.conn.commit()

    def save_calculation(self, data_tuple):
        query = """INSERT INTO calculations 
                   (bill_amount, tax_percent, tip_percent, people_count, total_sum, per_person, created_at)
                   VALUES (?, ?, ?, ?, ?, ?, ?);"""
        self.cursor.execute(query, data_tuple)
        self.conn.commit()
        return self.cursor.lastrowid

    def get_all_calculations(self):
        self.cursor.execute("SELECT * FROM calculations ORDER BY created_at DESC;")
        return self.cursor.fetchall()

    def update_calculation(self, calc_id, data_tuple):
        query = """UPDATE calculations SET 
                   bill_amount=?, tax_percent=?, tip_percent=?, people_count=?, total_sum=?, per_person=?
                   WHERE id=?;"""
        full_data = data_tuple + (calc_id,)
        self.cursor.execute(query, full_data)
        self.conn.commit()

    def delete_calculation(self, calc_id):
        query = "DELETE FROM calculations WHERE id=?;"
        self.cursor.execute(query, (calc_id,))
        self.conn.commit()

    def close(self):
        self.conn.close()