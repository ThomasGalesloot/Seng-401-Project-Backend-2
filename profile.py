from flask import Flask, render_template, request, flash

from Comment import Comment
from CommentData import CommentData
from Login import Login
from Post import Post
from PostData import PostData
from PostDatabase import Database

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

x = "hi"


@app.route("/profile")
def profile():
    return render_template("profile.html")


@app.route('/', methods=['POST'])
def getvalue():
    Username = request.form['uname']
    Password = request.form['psw']
    Test = Login(Username, Password)
    Test.compare()
    global x
    x = Username
    print(Test.confirm_found)
    if Test.confirm_found == "true":
        pst = Post()
        pst.retrieveBrowsingPosts()
        recipes = pst.retrievedPosts
        print(len(recipes))

        return render_template("main-page.html", len=len(recipes), recipes=recipes)
    else:
        flash('Invalid Credentials, please try again')
        return render_template("profile.html")


@app.route('/comment', methods=['POST'])
def postComment():
    title = request.form['title']
    content = request.form['content']
    author = "me"
    comment = Comment(title, content, author, 0, 0)  # TODO figure out how to find parentID
    comment.addComment()

    # needed for when the page refreshes?
    pst = Post()
    pst.retrieveBrowsingPosts()
    recipes = pst.retrievedPosts
    print(len(recipes))

    return render_template("main-page.html", len=len(recipes), recipes=recipes)


@app.route('/post', methods=['POST'])
def postPost():
    name = request.form['name']
    type = request.form['type']
    des = request.form['des']
    steps = request.form['steps']
    ing = request.form['ing']
    time = request.form['time']
    owner = "me"
    post = PostData(name, x, type, des, steps, ing, time)
    # print(" " + name + " " + x + " " + type + " " + des + " " + steps + " " + ing + " " + time)

    pst = Post()
    pst.pD = post
    pst.insertPost()
    pst.retrieveBrowsingPosts()
    recipes = pst.retrievedPosts
    print(len(recipes))

    return render_template("main-page.html", len=len(recipes), recipes=recipes)


@app.route('/viewPost', methods=['GET', 'POST'])
def viewPost():
    id = request.form["postId"]
    print(id)
    pst = Post()
    pst.retrieveBrowsingPosts()
    recipes = pst.retrievedPosts

    return render_template("main-page.html", len=len(recipes), recipes=recipes)


if __name__ == "__main__":
    app.run()
