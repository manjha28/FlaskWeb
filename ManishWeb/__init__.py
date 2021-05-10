from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

#Basically a dictionary which take a key value as the name by which we want to store the DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pythonweb.db'
db = SQLAlchemy(app)

from ManishWeb import routes