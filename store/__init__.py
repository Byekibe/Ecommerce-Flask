from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
app.config['SECRET_KEY'] = "HLBVGRHJBJKLIKYNGUEIN58P5JKFJKKJKLJJLK 845677896949"
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

from store.admin import routes
