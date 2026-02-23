from flask import Flask, render_template, request, redirect
import os
import psycopg2
from cryptography.fernet import Fernet

app = Flask(__name__)

# Configuration PostgreSQL
DB_HOST = os.environ.get('DB_HOST', 'postgres-service')
DB_NAME = os.environ.get('DB_NAME', 'identifiants')
DB_USER = os.environ.get('DB_USER', 'admin')
DB_PASS = os.environ.get('DB_PASS', 'password123')

# Chiffrement
KEY_FILE = "secret.key"
if os.path.exists(KEY_FILE):
    with open(KEY_FILE, "rb") as f:
        KEY = f.read()
else:
    KEY = Fernet.generate_key()
    with open(KEY_FILE, "wb") as f:
        f.write(KEY)

cipher = Fernet(KEY)

def get_db():
    return psycopg2.connect(
        host=DB_HOST, database=DB_NAME,
        user=DB_USER, password=DB_PASS
    )

def init_db():
    conn = get_db()
    cur = conn.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS identifiants
                 (id SERIAL PRIMARY KEY,
                  site TEXT NOT NULL,
                  login TEXT NOT NULL,
                  password TEXT NOT NULL)''')
    conn.commit()
    cur.close()
    conn.close()

def encrypt(password):
    return cipher.encrypt(password.encode()).decode()

def decrypt(password):
    return cipher.decrypt(password.encode()).decode()

@app.route('/')
def index():
    conn = get_db()
    cur = conn.cursor()
    cur.execute('SELECT * FROM identifiants')
    items_raw = cur.fetchall()
    cur.close()
    conn.close()
    items = [(i[0], i[1], i[2], decrypt(i[3])) for i in items_raw]
    return render_template('index.html', items=items)

@app.route('/add', methods=['POST'])
def add():
    site = request.form['site']
    login = request.form['login']
    password = encrypt(request.form['password'])
    conn = get_db()
    cur = conn.cursor()
    cur.execute('INSERT INTO identifiants (site, login, password) VALUES (%s, %s, %s)',
                (site, login, password))
    conn.commit()
    cur.close()
    conn.close()
    return redirect('/')

@app.route('/delete/<int:id>')
def delete(id):
    conn = get_db()
    cur = conn.cursor()
    cur.execute('DELETE FROM identifiants WHERE id = %s', (id,))
    conn.commit()
    cur.close()
    conn.close()
    return redirect('/')

if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=5000)