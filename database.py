import sqlite3

def create_database():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS employees (
            id INTEGER PRIMARY KEY,
            username TEXT NOT NULL,
            password TEXT NOT NULL,
            name TEXT NOT NULL,
            salary REAL NOT NULL,
            tenure INTEGER NOT NULL,
            leaves INTEGER NOT NULL,
            sick_leaves INTEGER NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

create_database()
