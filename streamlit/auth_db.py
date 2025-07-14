import streamlit as st
import mysql.connector

secrets = st.secrets["mysql"]
conn = mysql.connector.connect(
    host=secrets["localhost"],
    user=secrets["root"],
    password=secrets["cseds@32"],
    database=secrets["project2"]
)

csr = conn.cursor()
