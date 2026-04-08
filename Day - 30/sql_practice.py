import sqlite3
conn=sqlite3.connect("practice.db")
cursor=conn.cursor()
cursor.execute("""
    SELECT * FROM employees
    WHERE salary > 90000
""")
rows=cursor.fetchall()
for row in rows:
    print(row)
conn.close()