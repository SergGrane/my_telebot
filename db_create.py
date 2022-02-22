
import sqlite3
conn = sqlite3.connect('telebot.db')
cur = conn.cursor()
cur.execute("""CREATE TABLE 
   userid (INT PRIMARY KEY,
   fname TEXT,
   lname TEXT,
   phone TEXT,
   email TEXT);
""")
conn.commit()
#IF NOT EXISTS user