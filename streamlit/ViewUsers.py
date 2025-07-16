import streamlit as st
import pandas as pd
from auth_db import conn  # connection from your secrets

st.title("Registered Users")

try:
    # Read all users from signup_us
    df = pd.read_sql("SELECT * FROM signup_us", conn)

    if df.empty:
        st.info("No users found.")
    else:
        st.subheader("All Users")
        st.dataframe(df)

except Exception as e:
    st.error("Failed to fetch users.")
    st.exception(e)
