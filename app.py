from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_mysqldb import MySQL
import MySQLdb.cursors

app = Flask(__name__)
app.secret_key = 'many random bytes'

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'teacher_db'

mysql = MySQL(app)


@app.route('/')
@app.route('/login', methods=['GET', 'POST'])
def login():
    msg = ''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute(
            'SELECT * FROM users WHERE username = %s AND password = %s', (username, password,))
        account = cursor.fetchone()
        if account:
            session['loggedin'] = True
            session['id'] = account['id']
            session['username'] = account['username']
            msg = 'Logged in successfully!'
            return redirect(url_for('Index'))
        else:
            msg = 'Incorrect username/password!'
    return render_template('login.html', msg=msg)


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        cur = mysql.connection.cursor()
        cur.execute(
            "INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
        mysql.connection.commit()
        cur.close()

        return redirect(url_for('login'))
    return render_template('register.html')


@app.route('/logout')
def logout():
    session.pop('loggedin', None)
    session.pop('id', None)
    session.pop('username', None)
    return redirect(url_for('login'))


@app.route('/index')
def Index():
    if 'loggedin' in session:
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM teachers")
        teachers = cur.fetchall()
        cur.close()
        return render_template('index.html', teachers=teachers)
    return redirect(url_for('login'))


@app.route('/insert', methods=['POST'])
def insert():
    if request.method == 'POST':
        name = request.form['name']
        year_grad = request.form['year_grad']
        rank = request.form['rank']
        expe = request.form['expe']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO teachers (name, year_grad, rank, expe) VALUES (%s, %s, %s, %s)",
                    (name, year_grad, rank, expe))
        mysql.connection.commit()
        cur.close()
        flash("Data Inserted Successfully")
        return redirect(url_for('Index'))


@app.route('/delete/<int:id_data>', methods=['GET'])
def delete(id_data):
    flash("Record Has Been Deleted Successfully")
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM teachers WHERE id=%s", (id_data,))
    mysql.connection.commit()
    return redirect(url_for('Index'))


@app.route('/update', methods=['POST'])
def update():
    if request.method == 'POST':
        id = request.form['id']
        name = request.form['name']
        year_grad = request.form['year_grad']
        rank = request.form['rank']
        expe = request.form['expe']

        cur = mysql.connection.cursor()
        cur.execute("""
               UPDATE teachers
               SET name=%s, year_grad=%s, rank=%s, expe=%s
               WHERE id=%s
            """, (name, year_grad, rank, expe, id))
        flash("Data Updated Successfully")
        mysql.connection.commit()
        cur.close()
        return redirect(url_for('Index'))


if __name__ == "__main__":
    app.run()
