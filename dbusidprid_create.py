import sqlite3
conn = sqlite3.connect('orders.db')
cur = conn.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS usidprid(
   usprid TEXT PRIMARY KEY,
   usid INT ,
   prid INT
   );
""")
conn.commit()



cur.execute("select * from usidprid")
results = cur.fetchall()
print(results)