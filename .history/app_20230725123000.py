## create a simple flask application

from flask import Flask,render_template
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
    return render_template('index.html')


@app.route('/success/<int:score>')
def success (score):
    return "the person is passed and the score is "+str(score)
    
@app.route('/fail/<int:score>')
def fail (score):
    return "the person has failed  and the score is "+str(score)







if __name__=='__main__':
    app.run(debug=True)