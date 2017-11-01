from flask import Flask,request

app = Flask(__name__)



@app.route("/profile/")
def index():
    return ("request method:%s" % request.method)


@app.route("/profile/method",methods=['GET','POST'])
def method():
    if request.method == "POST":
        return 'you usering method:POST'
    else:
        return 'you usering method:GET'






if __name__ == "__main__":
    app.run()