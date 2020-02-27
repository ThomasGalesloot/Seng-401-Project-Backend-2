from flask import Flask, render_template, request
from Login import Login
from Database import Database
app = Flask(__name__)


@app.route("/profile")
def profile():
    return render_template("profile.html")


@app.route('/', methods=['POST'])
def getvalue():
    Username = request.form['uname']
    Password = request.form['psw']
    Test = Login(Username, Password)
    Test.compare()
    print(Test.confirm_found)
    if Test.confirm_found == "true":
        return render_template("Welcom.html")
    else:
        return render_template("NoGood.html")


if __name__ == "__main__":
    app.run()

