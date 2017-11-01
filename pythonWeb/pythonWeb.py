from flask import Flask,request

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World! %s' % request.method

@app.route("/index")
def index():
    return  '<h1>This is index page</h1>'

@app.route("/user/<name>")
def user_name(name):
    return 'My name is: %s'%name


@app.route("/user/<int:id>")
def user_id(id):
    return 'My id is: %d'%id

if __name__ == '__main__':
    app.run(debug=True)
