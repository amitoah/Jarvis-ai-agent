import sqlite3


conn = sqlite3.connect('amishra.db')
cursor = conn.cursor()

query = "CREATE TABLE IF NOT EXISTS sys_command(id integer primary key, name VARCHAR(100), path VARCHAR(1000))"
cursor.execute(query)


# query = "INSERT INTO SYS_COMMAND VALUES (null, 'mx excel', 'C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Office\\ Microsoft Excel.lnk')"
# cursor.execute(query)
# conn.commit()

query = "CREATE TABLE IF NOT EXISTS web_command(id integer primary key, name VARCHAR(100), url VARCHAR(1000))"
cursor.execute(query)

query = "INSERT INTO web_COMMAND VALUES (null, 'youtube', 'https://www.youtube.com/')"
cursor.execute(query)
conn.commit()