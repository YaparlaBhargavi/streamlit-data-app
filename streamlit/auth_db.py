import mysql.connector
import streamlit as st

# ✅ Fetch credentials from secrets
secrets = st.secrets["mysql"]

# ✅ Create database connection
conn = mysql.connector.connect(
    host=secrets["host"],
    user=secrets["user"],
    password=secrets["cseds@32"],
    database=secrets["project2"]
)

# ✅ Create cursor
csr = conn.cursor()
