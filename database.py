import sqlite3

connection = sqlite3.connect("incidents.db")

cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS incidents (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    employee_name TEXT,
    incident_type TEXT,
    description TEXT
)
""")

connection.commit()
connection.close()

print("Database created successfully.")