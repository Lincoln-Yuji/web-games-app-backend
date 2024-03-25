from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

# Initialize the flask application
app = Flask(__name__, static_folder="./frontend", static_url_path="/")
CORS(app)

# Connect to the Python Anywhere MySQL data base
_USER = "lincolnyuji"
_PASS = "root1234"
_HOST = "lincolnyuji.mysql.pythonanywhere-services.com"
_BASE = "lincolnyuji$webgames"

# app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+mysqlconnector://root:root@localhost/webgames"
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+mysqlconnector://{}:{}@{}/{}".format(_USER, _PASS, _HOST, _BASE)
app.config["SQLALCHEMY_TRACK_MODIFIATIONS"] = False

db = SQLAlchemy(app)