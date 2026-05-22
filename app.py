from flask import Flask, render_template, request, redirect, session, send_from_directory
import sqlite3
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.secret_key = "cloud_secret_key"

UPLOAD_FOLDER = "uploads"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# ------------------ HOME ------------------
@app.route('/')
def home():
    return redirect('/login')


# ------------------ REGISTER ------------------
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']

        conn = sqlite3.connect('database.db')
        cur = conn.cursor()

        cur.execute("INSERT INTO users (name,email,password) VALUES (?,?,?)",
                    (name, email, password))

        conn.commit()
        conn.close()

        return redirect('/login')

    return render_template("register.html")


# ------------------ LOGIN ------------------
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        conn = sqlite3.connect('database.db')
        cur = conn.cursor()

        cur.execute("SELECT * FROM users WHERE email=? AND password=?",
                    (email, password))

        user = cur.fetchone()
        conn.close()

        if user:
            session['user_id'] = user[0]
            return redirect('/dashboard')

        return "Invalid Login"

    return render_template("login.html")


# ------------------ LOGOUT ------------------
@app.route('/logout')
def logout():
    session.clear()
    return redirect('/login')


# ------------------ DASHBOARD ------------------
@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect('/login')

    conn = sqlite3.connect('database.db')
    cur = conn.cursor()

    cur.execute("SELECT * FROM files WHERE user_id=?", (session['user_id'],))
    files = cur.fetchall()

    conn.close()

    return render_template("dashboard.html", files=files)


# ------------------ UPLOAD FILE ------------------
@app.route('/upload', methods=['POST'])
def upload():
    if 'user_id' not in session:
        return redirect('/login')

    file = request.files['file']
    filename = secure_filename(file.filename)

    path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(path)

    conn = sqlite3.connect('database.db')
    cur = conn.cursor()

    cur.execute("INSERT INTO files (user_id, filename, filepath) VALUES (?,?,?)",
                (session['user_id'], filename, path))

    conn.commit()
    conn.close()

    return redirect('/dashboard')


# ------------------ DOWNLOAD FILE ------------------
@app.route('/download/<filename>')
def download(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename, as_attachment=True)


# ------------------ DELETE FILE ------------------
@app.route('/delete/<filename>')
def delete(filename):
    if 'user_id' not in session:
        return redirect('/login')

    conn = sqlite3.connect('database.db')
    cur = conn.cursor()

    cur.execute("DELETE FROM files WHERE filename=? AND user_id=?",
                (filename, session['user_id']))

    conn.commit()
    conn.close()

    path = os.path.join(app.config['UPLOAD_FOLDER'], filename)

    if os.path.exists(path):
        os.remove(path)

    return redirect('/dashboard')


# ------------------ RUN APP ------------------
if __name__ == '__main__':
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)

    app.run(debug=True)