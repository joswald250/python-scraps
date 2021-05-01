from flask import Flask, render_template, request
from flask_mysqldb import MySQL
import datetime

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'user'
app.config['MYSQL_PASSWORD'] = 'password'
app.config['MYSQL_DB'] = 'name of database'

mysql = MySQL(app)


@app.route('/', methods=['GET', 'POST'])
def users():
    if request.method == "POST":
        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO accounts(username, password, creation_datetime, email)
                    VALUES ({}, {}, {})'.format('username', 'password', datetime.datetime))
        mysql.connection.commit()
        rv = cur.fetchall()
        cur.close()
        return str(rv)
    return render_template('login.html')


if __name__ == '__main__':
    app.run(debug=False)
