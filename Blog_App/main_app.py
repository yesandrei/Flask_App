#This is a blog app that allows users to register and post blogs
from datetime import datetime
from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

#how we configure different things for the app, protects from attacks? encrpyts the password
app.config['SECRET_KEY'] = '47157c05fffe096d630b9d5d37d03e3e'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.string(20), unique=True, nullable=False)
    email = db.Column(db.string(120), unique=True, nullable=False)
    image_file = db.Column(db.string(20), nullable=False, default='default.jpg')
    password = db.Column(db.string(60), nullable=False)
#repr = reprint
    def __repr__(self):
        return f"User('{self.username}' '{self.email}', {self.image_file}
#flask also makes python able to put python programming inside an html document

posts = [
    
    {
        'author':'Andrei M',
        'title':'Blog Post 1',
        'content':'First Post Content',     
        'date_posted':'Febuary 2 2022'
    },
    
    {
        'author':'Jane Doe',
        'title':'Blog Post 2',
        'content':'Second Post Content',     
        'date_posted':'Febuary 4 2022'
    },
    
    {
        'author':'Hannah Bloggs',
        'title':'Blog Post 3',
        'content':'Third Post Content',     
        'date_posted':'Febuary 6 2022'
    }
    
]

#The below code links everything to the other html files in the folder.
#If theres nothing when it links it will link to the home page.
@app.route("/")
@app.route("/home")
def home():
#post=posts puts the posts variable into the html file so we can use it
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
#passing the title so that the title of the website changes only for about
    return render_template('about.html', title="About")

#route for registration page
@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!',  'success')
        return redirect(url_for('home'))
#flash format will put in the username variable so that the message comes up with the persons name.
    return render_template('register.html', title="Register", form=form)

#route for login page
@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check your email and password', 'danger')
    return render_template('login.html', title="Login", form=form)

#Makes it able to run in debugging mode ( so when you save it refreshes the website )
if __name__=='__main__':
    app.run(debug=True)