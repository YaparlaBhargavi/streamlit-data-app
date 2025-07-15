import mysql.connector
import streamlit as st

# Load MySQL secrets
secrets = st.secrets["mysql"]

# Connect to Railway-hosted MySQL
conn = mysql.connector.connect(
    host=secrets["host"],
    port=int(secrets["port"]),  # Ensure port is treated as integer
    user=secrets["user"],
    password=secrets["password"],
    database=secrets["database"]
)

csr = conn.cursor()
