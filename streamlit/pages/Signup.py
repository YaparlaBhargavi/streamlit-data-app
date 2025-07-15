import streamlit as st
from auth_db import conn, csr  # make sure both are imported

st.title("Sign Up Here")

col1, col2 = st.columns(2)

with col1:
    username = st.text_input("Enter Your Unique Name")
with col2:
    full_name = st.text_input("Enter Your Full Name")

phone = st.text_input("Enter Your Phone Number")
email = st.text_input("Enter Your Email Address")
passwordd = st.text_input("Enter Your Password", type="password")
conform_pass = st.text_input("Confirm Password", type="password")
btn = st.button("Sign Up")

if btn:
    if username == "" or full_name == "" or phone == "" or email == "" or passwordd == "" or conform_pass == "":
        st.error("Please fill up all the fields.")
        st.snow()
    else:
        if passwordd != conform_pass:
            st.warning("Passwords do not match.")
            st.snow()
        else:
            try:
                csr.execute(f"insert into signup_us(username,full_name,phone,email,passwordd) values('{username}','{full_name}','{phone}','{email}','{passwordd}')")
                conn.commit()
                st.success("Account created successfully")
                st.balloons()

                # ✅ Correct Login Page Link
                st.markdown('<a href="./Login" target="_self">Click here to Login</a>', unsafe_allow_html=True)

            except Exception:
                st.error("Please check — username must be unique or check database structure!")
  

