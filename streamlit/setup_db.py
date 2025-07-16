from auth_db import conn, csr

def db_setup():
    csr.execute("""
    CREATE TABLE IF NOT EXISTS signup_us (
        username VARCHAR(120) UNIQUE,
        Full_name VARCHAR(255),
        phone VARCHAR(12),
        email VARCHAR(255),
        passwordd VARCHAR(255)
    )
    """)

    conn.commit()