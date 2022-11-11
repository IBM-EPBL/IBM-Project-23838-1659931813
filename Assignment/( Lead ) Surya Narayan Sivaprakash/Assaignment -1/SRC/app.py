from tkinter.tix import Form
from flask import Flask ,render_template,url_for,redirect,request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")
@app.route('/success/<name>/<phone>/<email>')
def success(name=None,phone=None,email=None):
    return "<body style='  background-color: white;display: flex;flex-direction: column;align-items: center;justify-content: center;'><form style='    display: flex;flex-direction: column;align-items: center;justify-content: center;background-color:#dcdcdc;width: 40%;height: 500px;border-radius: 20px;margin: 100px;'> <h1>Sign Up Completed</h1><h2>Details</h2> Name:  {} <br> Email:  {} <br>Phone Number:  {} </form></body>".format(name ,email, phone)

@app.route("/login",methods =['POST','GET'])
def login():
    if request.method == 'POST':
        user = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        return redirect(url_for("success", name = user ,phone = phone ,email = email ))
    else:
        user = request.args.get("input_name")
        return redirect(url_for("success",name=user))


if __name__ == '__main__':
    app.run(debug=True)
