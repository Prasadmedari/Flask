## create a simple flask application

from flask import Flask
## create the flask app

app=Flask(__name__)

@app.route('/')
def home():
    







if __name__=='__main__':
    app.run()