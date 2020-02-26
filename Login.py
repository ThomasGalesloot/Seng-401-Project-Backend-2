from flask import Flask, request, render_template

from Database import Database


# this is a simple test of the db feature
class Login:
    username = ""
    password = ""
    db = Database()
    confirm_found = "false"

    def __init__(self, na, pa):
        self.username = na
        self.password = pa

    def compare(self):
        rowcount = self.db.cursor.execute('select * from Users.dbo.login_info WHERE username =? AND password = ?',
                                          (self.username, self.password))

        rows = rowcount.fetchone()
        print(rows)
        if rows is None:
            self.confirm_found = "false"
        else:
            self.confirm_found = "true"


app = Flask(__name__)


@app.route("/profile")
def profile():
    return render_template("profile.html")


@app.route('/', methods=['POST'])
def getvalue():
    Username = request.form['uname']
    Password = request.form['psw']
    Test = Login(Username,Password)


if __name__ == "__main__":
    app.run()

