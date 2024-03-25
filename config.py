from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

# Initialize the flask application
app = Flask(__name__, static_folder="./frontend", static_url_path="/")
CORS(app)

# Set the location of the database creation and its name
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///mydatabase.db"
app.config["SQLALCHEMY_TRACK_MODIFIATIONS"] = False

db = SQLAlchemy(app)