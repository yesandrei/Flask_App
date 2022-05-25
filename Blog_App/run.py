from main_app import app

#Makes it able to run in debugging mode ( so when you save it refreshes the website )
if __name__=='__main__':
    app.run(debug=True)