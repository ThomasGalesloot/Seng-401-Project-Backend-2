from flask import Flask, render_template, request, flash

from Comments import Comments
from Login import Login
from Database import Database

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'


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
        flash('Invalid Credentials, please try again')
        return render_template("profile.html")


@app.route('/postComment', methods=['GET', 'POST'])
def postComment():
    title = request.form['title']
    content = request.form['content']
    Test = Comments(title, content)
    Test.addComment()
    return render_template("profile.html")

if __name__ == "__main__":
    app.run()
