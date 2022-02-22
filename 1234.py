
import sqlite3

conn = sqlite3.connect('telebot.db')
cur = conn.cursor()
#d='Grane'
cur.execute("SELECT * FROM user")
#sql = "SELECT * FROM user WHERE fname =?"
#cur.execute(sql, [(d)])
#print(cur.fetchall())
results = cur.fetchall()
print(results)