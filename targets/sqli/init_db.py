import sqlite3

def init_db():
    conn = sqlite3.connect('test.db')
    cursor = conn.cursor()

    # Users table (public)
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT,
            role TEXT
        )
    ''')

    # Secrets table (Ground Truth)
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS secrets (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            flag TEXT
        )
    ''')

    # Populate with test data
    cursor.execute("INSERT INTO users (username, role) VALUES ('admin', 'administrator')")
    cursor.execute("INSERT INTO users (username, role) VALUES ('john', 'user')")
    
    # Insert the flag
    cursor.execute("INSERT INTO secrets (flag) VALUES ('CTF{SQLi_Master_Agent_2026}')")

    conn.commit()
    conn.close()
    print("Database initialized successfully.")

if __name__ == '__main__':
    init_db()