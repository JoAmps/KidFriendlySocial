import os
from flask import request, render_template, redirect, url_for, session, jsonify, Blueprint
from authentication_service.tokens import AccessTokens
from dotenv import load_dotenv
import bcrypt
import re
from functools import wraps
auth_bp = Blueprint('auth_bp', __name__, template_folder='templates', static_folder='static')
load_dotenv()
from main import mysql


@auth_bp.route('/')
def home():
    # Check if user is loggedin
    if 'loggedin' in session:
        # User is loggedin show them the home page
        return render_template('index.html', email=session['email'])
    # User is not loggedin redirect to login page
    return redirect(url_for('auth_bp.login'))


@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    # Output message if something goes wrong...
    msg = ''
    # Check if "username", "password" and "email" POST
    # requests exist (user submitted form)
    if request.method == 'POST' and 'email'\
            in request.form and 'password' in request.form:
        # Create variables for easy access
        email = request.form['email']
        password = request.form['password']
        hashed_password = bcrypt.hashpw(password.encode("utf-8"),
                                        bcrypt.gensalt())
        # Check if account exists using MySQL
        cursor = mysql.connection.cursor()
        cursor.execute('SELECT * FROM user WHERE email = %s', (email,))
        account = cursor.fetchone()
        # If account exists show error and validation checks
        if account:
            msg = 'Account already exists!'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            msg = 'Invalid email address!'
        elif not password or not email:
            msg = 'Please fill out the form!'
        else:
            # Account doesnt exists and the form data is valid,
            # now insert new account into user table
            cursor.execute('INSERT INTO user VALUES (NULL, %s, %s)',
                           (email, hashed_password))
            mysql.connection.commit()
            msg = 'You have successfully registered!'
    elif request.method == 'POST':
        # Form is empty... (no POST data)
        msg = 'Please fill out the form!'
    # Show registration form with message (if any)
    return render_template('register.html', msg=msg)


@auth_bp.route("/login", methods=['GET', 'POST'])
def login():
    msg = ''
    if request.method == 'POST' and 'email' in request.form and\
       'password' in request.form:
        email = request.form['email']
        password = request.form['password']
        auth = request.authorization
        if auth:
            return "missing credentials", 401
        # check for username and password in database
        cur = mysql.connection.cursor()
        cur.execute('SELECT * FROM user WHERE email= %s', (email,))
        account = cur.fetchone()

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
                session['token'] = token
                return redirect(url_for('ml_bp.inference'))
            # if not
            else:
                return jsonify({"error": "invalid credentials"})

        else:
            # Account doesnt exist or username/password incorrect
            msg = 'Incorrect username/password!'
    return render_template('index.html', msg=msg)


# Decorator for authentication
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None

        if 'Authorization' in request.headers:
            auth_header = request.headers['Authorization']
            token = auth_header.split(" ")[1]

        if not token:
            return jsonify({'message': 'Token is missing!'}), 401

        try:
            data = AccessTokens.decode_access_token(token, os.environ.get("SECRET"))
            current_user = data['email']
        except BaseException:
            return jsonify({'message': 'Token is invalid!'}), 401

        return f(current_user, *args, **kwargs)

    return decorated


@auth_bp.route('/feedback', methods=['POST'])
def feedback():
    if request.method == 'POST':
        if 'token' not in session:
            return redirect(url_for('login'))
        text = request.form['tweet']
        feedback = request.form['feedback']
        prediction = request.form['prediction']
        prediction = prediction[15:27]
        cursor = mysql.connection.cursor()
        cursor.execute('INSERT INTO feedbacks VALUES (NULL, %s, %s, %s)',
                       (text, prediction, feedback))
        mysql.connection.commit()
        message = 'You have successfully given the feedback, Thanks!'
        return render_template('predict.html', message=message)
