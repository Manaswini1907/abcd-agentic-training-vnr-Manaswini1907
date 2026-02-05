from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
CORS(app)   # ✅ Allows frontend (HTML/JS) to talk to backend

# -----------------------------
# Database connection function
# -----------------------------
def get_db_connection():
    conn = sqlite3.connect('portfolio.db')
    conn.row_factory = sqlite3.Row
    return conn

# -----------------------------
# Initialize database (run once)
# -----------------------------
@app.route('/init')
def init_db():
    conn = get_db_connection()
    conn.execute('''
        CREATE TABLE IF NOT EXISTS messages (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            message TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()
    return "Database Initialized"

# -----------------------------
# Contact form API
# -----------------------------
@app.route('/contact', methods=['POST'])
def contact():
    data = request.get_json()

    name = data.get('name')
    email = data.get('email')
    message = data.get('message')

    conn = get_db_connection()
    conn.execute(
        'INSERT INTO messages (name, email, message) VALUES (?, ?, ?)',
        (name, email, message)
    )
    conn.commit()
    conn.close()

    return jsonify({"status": "Message saved successfully"})

# -----------------------------
# Run the app
# -----------------------------
if __name__ == '__main__':
    app.run(debug=True)
