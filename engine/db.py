import sqlite3


conn = sqlite3.connect('amishra.db')
cursor = conn.cursor()

query = "CREATE TABLE IF NOT EXISTS sys_command(id integer primary key, name VARCHAR(100), path VARCHAR(100), path VARCHAR(1000))"
cursor.execute(query)
