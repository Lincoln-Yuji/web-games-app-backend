from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

# Initialize the flask application
app = Flask(__name__, static_folder="./frontend", static_url_path="/")
CORS(app)

# The data base configuration SHOULD NOT be inside the development project.
# We need to get the connection information from outside.
import sys
import os

current_dir = os.path.dirname(os.path.realpath(__file__))
parent_dir  = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from databaseconfig.db_config import db_info

_USER = db_info["user"]
_PASS = db_info["pass"]
_HOST = db_info["host"]
_BASE = db_info["base"]

# Connect to the Python Anywhere MySQL data base
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+mysqlconnector://{}:{}@{}/{}".format(_USER, _PASS, _HOST, _BASE)
app.config["SQLALCHEMY_TRACK_MODIFIATIONS"] = False

db = SQLAlchemy(app)