from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('test.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def home():
    return jsonify({"message": "Target API is running. Use /user?id=1 to check users."})

# -------------------------------------------------------------
# VULNERABLE ENDPOINT: SQL Injection (CWE-89)
# -------------------------------------------------------------
@app.route('/user', methods=['GET'])
def get_user():
    user_id = request.args.get('id', '')
    
    if not user_id:
        return jsonify({"error": "Missing 'id' parameter"}), 400

    conn = get_db_connection()
    cursor = conn.cursor()

    # Direct concatenation: UNION-based SQLi
    query = f"SELECT id, username, role FROM users WHERE id = {user_id}"

    try:
        cursor.execute(query)
        rows = cursor.fetchall()
        
        users = []
        for row in rows:
            users.append({"id": row["id"], "username": row["username"], "role": row["role"]})
            
        return jsonify({"status": "success", "data": users})
    except sqlite3.Error as e:
        # Return SQL-error (as a hint for attackers)
        return jsonify({"status": "error", "message": str(e)}), 500
    finally:
        conn.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)