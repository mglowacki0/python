import sqlite3

conn = sqlite3.connect('data/library.db')
cur = conn.cursor()
cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cur.fetchall()
print("Tabele w bazie:", tables)
conn.close()
