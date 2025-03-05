import sqlite3

def create_table():
    con = sqlite3.connect("user.db")
    cur = con.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS user (_id INTEGER PRIMARY KEY AUTOINCREMENT,  name TEXT NOT NULL, email TEXT UNIQUE NOT NULL, user_name TEXT NOT NULL UNIQUE, password TEXT NOT NULL, country TEXT NOT NULL)')
    con.commit()
    con.close()
create_table()