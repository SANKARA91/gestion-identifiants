from flask import Flask, render_template, request, redirect
import sqlite3
import os
from cryptography.fernet import Fernet

app = Flask(__name__)
DB = "identifiants.db"

# Génère ou charge la clé de chiffrement
KEY_FILE = "secret.key"
if os.path.exists(KEY_FILE):
    with open(KEY_FILE, "rb") as f:
        KEY = f.read()
else:
    KEY = Fernet.generate_key()
    with open(KEY_FILE, "wb") as f:
        f.write(KEY)

cipher = Fernet(KEY)

def encrypt(password):
    return cipher.encrypt(password.encode()).decode()

def decrypt(password):
    return cipher.decrypt(password.encode()).decode()

def init_db():
    conn = sqlite3.connect(DB)
    conn.execute('''CREATE TABLE IF NOT EXISTS identifiants
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  site TEXT NOT NULL,
                  login TEXT NOT NULL,
                  password TEXT NOT NULL)''')
    conn.commit()
    conn.close()

@app.route('/')
def index():
    conn = sqlite3.connect(DB)
    items_raw = conn.execute('SELECT * FROM identifiants').fetchall()
    conn.close()
    items = [(i[0], i[1], i[2], decrypt(i[3])) for i in items_raw]
    return render_template('index.html', items=items)

@app.route('/add', methods=['POST'])
def add():
    site = request.form['site']
    login = request.form['login']
    password = encrypt(request.form['password'])
    conn = sqlite3.connect(DB)
    conn.execute('INSERT INTO identifiants (site, login, password) VALUES (?, ?, ?)',
                 (site, login, password))
    conn.commit()
    conn.close()
    return redirect('/')

@app.route('/delete/<int:id>')
def delete(id):
    conn = sqlite3.connect(DB)
    conn.execute('DELETE FROM identifiants WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    return redirect('/')

if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=5000)