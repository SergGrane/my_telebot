import sqlite3
conn = sqlite3.connect('orders.db')
cur = conn.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS prod(
   prodid INT PRIMARY KEY,
   pname TEXT,
   pdesc TEXT,
   price int);
""")
conn.commit()

products = [
  ('00001', 'phone Samsung' , 'qweqweqweqweqweqweqeqew', 178),
  ('00002', 'phone Nokia', 'Dsasasasasa 00025', 2341),
    ('00003', '2020-01-07', '00016', 1123)
]

cur.executemany("INSERT INTO prod VALUES(?, ?, ?, ?);",products )

conn.commit()

cur.execute("select * from prod")
results = cur.fetchall()
print(results)