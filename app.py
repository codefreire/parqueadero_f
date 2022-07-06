from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:toor1234@localhost/pases_db'
app.secret_key = os.urandom(32)
app.config['SECRET_KEY'] = os.urandom(32)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from controllers.controllers import *

if __name__ == '__main__':
    app.run(debug=True)