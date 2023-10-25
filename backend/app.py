from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app= Flask(__name__)

# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://scott:tiger@localhost/mydatabase'

@app.route('/')
def hello_world():
    return 'world'

@app.route('/mathematics')
def hello_world():
    return 'hello mathematics'

@app.route('/english')
def hello_world():
    return 'hello english'

@app.route('/kiswahili')
def hello_world():
    return 'hello kiswahili'

@app.route('/science')
def hello_world():
    return 'hello science'

@app.route('/social_studies')
def hello_world():
    return 'social studies'

if __name__ =="__main__":
    app.run(debug=True)