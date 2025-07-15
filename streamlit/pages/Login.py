import streamlit as st 
from auth_db import csr

st.title("Login page")

username = st.text_input("Enter Your Username")
password = st.text_input("Enter Your Password", type="password")
btn = st.button("Login")

if btn:
    if username == "" or password == "":
        st.error("Please fill all fields.")
        st.snow()
    else:
        # ✅ Use parameterized query to avoid SQL injection
        csr.execute("SELECT * FROM signup_us WHERE username = %s", (username,))
        check_username = csr.fetchone()

        if check_username is None:
            st.warning("Username not found!")
        else:
            # ✅ check_username[4] = password column
            if password != check_username[4]:
                st.warning("Invalid password!")
            else:
                st.success("Login successful!")
                st.balloons()
                st.write(f"Welcome, **{check_username[1]}**")  # full_name
                 
