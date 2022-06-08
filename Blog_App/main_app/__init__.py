#This is a blog app that allows users to register and post blogs
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

app = Flask(__name__)

#how we configure different things for the app, protects from attacks? encrpyts the password
app.config['SECRET_KEY'] = '47157c05fffe096d630b9d5d37d03e3e'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)


from main_app import routes