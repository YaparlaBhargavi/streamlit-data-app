import streamlit as st 
from auth_db import conn, csr  # noqa: F401
import pandas as pd

st.title("My Web App")

# ✅ Optional: Show data from your DB
# Make sure your table name is correct (likely `signup_users`, not `signup_use`)
# query = "SELECT * FROM signup_users;"
# df = pd.read_sql(query, conn)
# st.subheader("Data from Database")
# st.dataframe(df)

my_file = st.file_uploader("Upload your file to view data", type=["csv", "xls", "xlsx"])

if my_file is not None:
        if my_file.name.endswith('.csv'):
            df = pd.read_csv(my_file)
        else:
            df = pd.read_excel(my_file)

        st.success("File uploaded and read successfully!")
        st.subheader("Preview of Uploaded Data")
        st.dataframe(df)
st.markdown(
    """
    <style>
    .stApp {
        background-image: url("https://wallpapercrafter.com/desktop1/518541-abstract-backgrounds-full-frame-green-color-no.jpg");
        background-size: cover;
    }
    </style>
    """,
    unsafe_allow_html=True
)