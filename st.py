import mysql.connector

# Connect to MySQL server
cnx = mysql.connector.connect(
    host='localhost',
    user='admin',
    password='123456'
)

# Create a new database if it doesn't exist
cursor = cnx.cursor()
cursor.execute("CREATE DATABASE IF NOT EXISTS Student")
cursor.close()

# Connect to the StudentDB database
cnx.database = 'Student'

# Create the Students table if it doesn't exist
cursor = cnx.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS Students (
        StudentID INT PRIMARY KEY,
        FirstName CHAR(20) NOT NULL,
        LastName CHAR(20),
        Level INT
    )
""")
cursor.close()

# Insert student data into the Students table
cursor = cnx.cursor()
students_data = [
    (6, 'Nada', 'Mohammed', 2),
    (7, 'Samia', 'Ali', 3),
    (8, 'Nora', 'Sami', 2),
    (9, 'Huda', 'Omar', 4)
]
cursor.executemany("INSERT INTO Students (StudentID, FirstName, LastName, Level) VALUES (%s, %s, %s, %s)", students_data)
cnx.commit()
cursor.close()

# Retrieve and print the details of the first three students
cursor = cnx.cursor()
cursor.execute("SELECT * FROM Students LIMIT 3")
students = cursor.fetchall()
for student in students:
    print(f"StudentID: {student[0]}, FirstName: {student[1]}, LastName: {student[2]}, Level: {student[3]}")
cursor.close()

# Close the database connection
cnx.close()