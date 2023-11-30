import sqlite3
from sqlite3 import Error

# Making sure I can successfully connect to the database
try:
    db = sqlite3.connect('student_db')
except Error:
    print(Error)

# Get a cursor object
cursor = db.cursor()  

# Creating the table and making sure I can still creat it even if it already exists (IF NOT EXISTS)
cursor.execute('''
    CREATE TABLE IF NOT EXISTS python_programming(
    id INTEGER PRIMARY KEY, 
    name TEXT,
    grade INTEGER)
''')

# Inserting records into the table
cursor.executescript('''
    INSERT OR IGNORE INTO python_programming VALUES(55, 'Carl Davis', 61);
    INSERT OR IGNORE INTO python_programming VALUES(66, 'Dennis Fredrickson', 88);
    INSERT OR IGNORE INTO python_programming VALUES(77, 'Jane Richards', 78);
    INSERT OR IGNORE INTO python_programming VALUES(12, 'Peyton Sawyer', 45);
    INSERT OR IGNORE INTO python_programming VALUES(2, 'Lucas Brooke', 99);                                                          
 ''')
db.commit()

# Retrieving all the data in the table
cursor.execute('''SELECT * FROM python_programming''')
for row in cursor:
    print('{0} | {1} | {2}'.format(row[0], row[1], row[2]))

# Retrieving a specific record
cursor.execute('''SELECT * FROM python_programming WHERE grade BETWEEN 60 AND 80 ''')
student = cursor.fetchone()
print(f"This is the student with a a grade between 60 and 80: {student}")

# Updating data
cursor.execute('''UPDATE python_programming SET grade = 65 WHERE name = 'Carl Davis' ''')

# Deleting a row
cursor.execute('''DELETE FROM python_programming WHERE name = 'Dennis Fredrickson' ''')

# Updating data
cursor.execute('''UPDATE python_programming SET grade = 80 WHERE id > 55 ''')

db.commit()


# Retrieving all the data in the table
print("------------This is the changed table-----------------")
cursor.execute('''SELECT * FROM python_programming''')
for row in cursor:
    print('{0} | {1} | {2}'.format(row[0], row[1], row[2]))



