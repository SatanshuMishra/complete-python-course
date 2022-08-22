import sqlite3
connection = sqlite3.connect('data.db')
connection.close()

cursor = connection.cursor()

cursor.execute('SQL QUERY HERE')
connection.commit()

connection.close()