from pdb import post_mortem
from flask import Flask, render_template
app = Flask(__name__)

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
    return render_template('about.html')

#Makes it able to run in debugging mode ( so when you save it refreshes the website )
if __name__=='__main__':
    app.run(debug=True)