from flask import Flask
from database import db


app = Flask(__name__)
db.init_app(app)
