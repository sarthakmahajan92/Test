import sqlite3

# Connect to SQLite database (or create it)
conn = sqlite3.connect("student.db")
cursor = conn.cursor()

# CREATE: Create a table named 'users'
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
  id INTEGER ,
  name TEXT,
  email TEXT
)
''')
conn.commit()

# INSERT into 'users' table (not 'student')
cursor.execute("INSERT INTO users VALUES (1, 'SARTHAK', 'sarthak12@gmail.com')")
conn.commit()

# READ from 'users' table
cursor.execute("SELECT * FROM users")
user = cursor.fetchall()

# Print all current users
print("All Current Users:", user)

# UPDATE 
# cursor.execute("UPDATE users SET name='SARTHAK' WHERE id=1")
# print("User Update")



conn.close()
