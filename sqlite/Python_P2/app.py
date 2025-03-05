from flask import Flask, jsonify
from flask import request
import sqlite3
app = Flask(__name__)

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    name=data.get('name')
    email=data.get('email')
    user_name=data.get('user_name')
    password=data.get('password')
    country=data.get('country')
    if not name or not email or not user_name or not password or not country:
        return jsonify({'message': 'All fields are required'})
    con = sqlite3.connect('user.db')
    cur = con.cursor()
    cur.execute("""
                INSERT INTO user (name, email, user_name, password, country)
                VALUES (?, ?, ?, ?, ?)
                """, (name, email, user_name, password, country))
    con.commit()
    con.close()
    return jsonify({'message': 'User registered successfully'})
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user_name = data.get('user_name')
    password = data.get('password')
    if not user_name or not password:
        return jsonify({'message': 'All fields are required'})
    con = sqlite3.connect('user.db')
    cur = con.cursor()
    cur.execute("""
                SELECT * FROM user WHERE user_name = ? AND password = ?
                """, (user_name, password))
    user = cur.fetchone()
    con.close()
    if user:
        return jsonify({'message': 'Login successful'})
    return jsonify({'message': 'Invalid credentials'})

if __name__ == '__main__':
    app.run(debug=True)