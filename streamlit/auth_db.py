import mysql.connector

# Create database connection
conn = mysql.connector.connect(
    host="localhost",       # or your DB host
    user="root",       # replace with your DB username
    password="cseds@32",   # replace with your DB password
    database="project2"      # replace with your DB name
)

# Create a cursor object
csr = conn.cursor()
