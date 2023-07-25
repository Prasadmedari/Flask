## create a simple flask application

from flask import Flask,redirect,url_for
## create the flask app

app=Flask(__name__)

@app.route('/')
def home():
    return "<h1>Hello, world!<h1>"


@app.route('/welcome')
def welcome():
    return "welcome to the Flask Turorials"

@app.route('/index')
def index():
    return redirect(url_for('index'))











if __name__=='__main__':
    app.run(debug=True)