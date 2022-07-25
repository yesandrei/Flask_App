#This is a blog app that allows users to register and post blogs
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)

#how we configure different things for the app, protects from attacks? encrpyts the password
app.config['SECRET_KEY'] = '47157c05fffe096d630b9d5d37d03e3e'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

from main_app import routes

#login view makes it so that u need to be logged into an account to access the account page. If not logged in it will send the user to the login page. The 'info' is bootstrap which makes it blue.