import os
from flask import Flask, request, session
from flask_mysqldb import MySQL
from dotenv import load_dotenv
import bcrypt
import re
import warnings
warnings.filterwarnings("ignore")
from tokens import AccessTokens


load_dotenv()
server = Flask(__name__)
mysql = MySQL(server)
server.secret_key = os.environ["SECRET"]
server.config["MYSQL_HOST"] = os.environ["MYSQL_HOST"]
server.config["MYSQL_USER"] = os.environ["MYSQL_USER"]
server.config["MYSQL_PASSWORD"] = os.environ["MYSQL_PASSWORD"]
server.config["MYSQL_DB"] = os.environ["MYSQL_DB"]
server.config["MYSQL_PORT"] = 25060


@server.route('/register', methods=['POST'])
def register():
    # Output message if something goes wrong...
    msg = ''
    # Check if "username", "password" and "email" POST
    # requests exist (user submitted form)
    # Create variables for easy access
    data = request.get_json()
    email = data.get("email")
    password = data.get('password')
    hashed_password = bcrypt.hashpw(password.encode("utf-8"),
                                    bcrypt.gensalt())
    # Check if account exists using MySQL

    db = mysql.connect
    cursor = db.cursor()
    cursor.execute('SELECT * FROM user WHERE email = %s', (email,))
    account = cursor.fetchone()
    if account:
        cursor.close()
        db.close()
        return "Account already exists!"

    elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
        msg = 'Invalid email address!'
        cursor.close()
        db.close()
        return msg

    elif not password or not email:
        msg = 'Please fill out the form!'
        cursor.close()
        db.close()
        return msg

    else:
        # Account doesnt exists and the form data is valid,
        # now insert new account into user table
        cursor.execute('INSERT INTO user VALUES (NULL, %s, %s)',
                       (email, hashed_password))
        db.commit()
        cursor.close()
        db.close()
        msg = 'You have successfully registered!'
        return msg


@server.route("/login", methods=['POST'])
def login():
    msg = ''
    data = request.get_json()
    email = data.get("email")
    password = data.get('password')
    # check for username and password in database
    db = mysql.connect
    cursor = db.cursor()
    cursor.execute('SELECT * FROM user WHERE email= %s', (email,))
    account = cursor.fetchone()

    if account:
        # if there's a user
        id = account[0]
        email = account[1]
        hashed_password = account[2]
        session['loggedin'] = True
        session['id'] = id
        session['email'] = email
        # If email is correct and passwords match
        if email and bcrypt.checkpw(password.encode('utf-8'),
                                    hashed_password.encode('utf-8')):
            token = AccessTokens.generate_access_token(
                email, os.environ.get("SECRET"), True)
            return {"token": token}
    else:
        # Account doesnt exist or username/password incorrect
        msg = 'Incorrect username/password!'
        return msg


if __name__ == "__main__":
    server.run(host="0.0.0.0", port=5050, debug=True)
