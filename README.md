# streamlit-data-app

# Data Reading App

**SmartStream** is a modern and easy-to-use web app built with **Streamlit**. It allows users to securely sign up and log in, connect to a MySQL database, and upload CSV or Excel files to preview their contents. The interface includes a custom background image and a responsive layout for a better user experience.

---

## 🚀 Features

- 🔐 User Sign-Up and Login system
- 🗃️ MySQL database integration for storing user details
- 📁 Upload CSV/XLS/XLSX files
- 📊 View uploaded data in a table
- 🎨 Clean UI with background image styling

---

## 📁 Project Structure

smartstream-app/
├── app.py               # Main file upload & viewer
├── auth_db.py           # MySQL database connection
├── pages/
│   ├── Login.py         # User login logic
│   └── Signup.py        # User signup logic
├── assets/
│   └── background.jpg   # Background image
├── requirements.txt     # Python dependencies
└── README.md            # Project documentation

## 💡 Future Enhancements

- 🔒 Password hashing (bcrypt)
- ✉️ Email verification or OTP login
- 📊 Admin dashboard and analytics
- 🧑‍💼 Role-based user access
