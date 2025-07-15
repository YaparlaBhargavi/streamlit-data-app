import mysql.connector
import streamlit as st

# ✅ Correct: Load the [mysql] group from secrets
secrets = st.secrets["mysql"]

# ✅ Access each key inside the group
conn = mysql.connector.connect(
    host=secrets["host"],         # example: "127.0.0.1" or cloud host
    user=secrets["user"],         # example: "root"
    password=secrets["password"], # example: "cseds@32"
    database=secrets["database"]  # example: "project2"
)

csr = conn.cursor()
