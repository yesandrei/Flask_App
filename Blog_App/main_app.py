from flask import Flask, render_template

app = Flask(__name__)

#The below code links everything to the other html files in the folder.
#If theres nothing when it links it will link to the home page.
@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/about")
def about():
    return render_template('about.html')

#Makes it able to run in debugging mode ( so when you save it refreshes the website )
if __name__=='__main__':
    app.run(debug=True)