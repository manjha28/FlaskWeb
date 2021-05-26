from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
app = Flask(__name__)

#Basically a dictionary which take a key value as the name by which we want to store the DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pythonweb.db'

#Secret Key for forms to display
app.config['SECRET_KEY'] = 'bc6c11f5d20b1bd40a381380'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login_page'
login_manager.login_message_category = 'info'
from ManishWeb import routes