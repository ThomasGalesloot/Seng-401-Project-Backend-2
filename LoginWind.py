from flask import render_template, Flask

import LoginForm

app = Flask(__name__)


# ...

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Sign In', form=form)


if __name__ == "__main__":
    app.run()
