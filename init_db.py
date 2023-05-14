import sqlite3

#You open a connection to a database file named database.db, which will be created once you run the Python file
conn = sqlite3.connect('database.db')

#use the open() function to open the schema.sql file. 
#Next you execute its contents using the executescript() method that executes multiple SQL statements at once, 
#which will create the tasks table.
with open('schema.sql') as f:
    conn.executescript(f.read())

cur = conn.cursor()

cur.execute("INSERT INTO tasks (task_name) VALUES (?)",
            ('Content for the first post',)
            )

conn.commit()
conn.close()