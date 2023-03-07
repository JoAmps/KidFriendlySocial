from flask import Flask
from ML_model.ml_routes import ml_bp
from authentication_service.auth_routes import auth_bp
from flask_mysqldb import MySQL
import os

server = Flask(__name__)
server.register_blueprint(auth_bp)
server.register_blueprint(ml_bp)

mysql = MySQL(server)
server.secret_key = os.environ["SECRET"]
server.config["MYSQL_HOST"] = os.environ["MYSQL_HOST"]
server.config["MYSQL_USER"] = os.environ["MYSQL_USER"]
server.config["MYSQL_PASSWORD"] = os.environ["MYSQL_PASSWORD"]
server.config["MYSQL_DB"] = os.environ["MYSQL_DB"]
server.config["MYSQL_PORT"] = 3306


if __name__ == "__main__":
    server.run(host="0.0.0.0", port=5050, debug=True)
