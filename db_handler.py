import sqlite3
from datetime import datetime, timedelta

class DBHandler:
    def __init__(self, dbname="dhcp", host="localhost", user="root", password="12345678"):
        self.conn = sqlite3.connect(dbname)

    def update_db(self, leases):
        cursor = self.conn.cursor()
        cursor.executemany("INSERT INTO leases VALUES (?,?,?,?)", leases)
        self.conn.commit()

    def get_unused_ips(self):
        one_year_ago = datetime.now() - timedelta(days=365)
        cursor = self.conn.cursor()
        cursor.execute("SELECT ip FROM leases WHERE lease_end < ?", (one_year_ago,))
        return cursor.fetchall()
