import mysql.connector

# Establish a connection to the MySQL server
conn = mysql.connector.connect(user='root', password='123456')

# Select the StudentDB database
conn.database = 'StudentDB'

# Create a cursor object
cursor = conn.cursor()

# Execute an SQL query
cursor.execute("SELECT * FROM Students")

# Fetch the results (for SELECT queries)
results = cursor.fetchone()
recordNum = cursor.rowcount
print("Total records fetched so far are:", recordNum)

results = cursor.fetchmany(3)
recordNum = cursor.rowcount
print("Total records fetched so far are:", recordNum)

# Close the cursor and connection
cursor.close()
conn.close()