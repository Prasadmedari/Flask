## create a simple flask application

from flask import Flask
## create the flask app

app=Flask(__name__)

@app.route('/')
def home():
    return "Hello world"


@app.route('/welcome')
def welcome():
    return "welcome to the Flask Turorials"

@app.route('/index')
def welcome():
    return "welcome to the index page"







if __name__=='__main__':
    app.run(debug=True)