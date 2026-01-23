import sqlite3

conn = sqlite3.connect('education.db')
cursor = conn.cursor()

with open('../backend/schema.sql', 'r', encoding='utf-8') as f:
    sql_script = f.read()

cursor.executescript(sql_script)
conn.commit()
conn.close()

print("Database initialized successfully.")
