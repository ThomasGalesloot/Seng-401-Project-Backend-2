from flask import Flask, render_template, request, flash

from Comment import Comment
from CommentData import CommentData
from Login import Login
from Post import Post
from PostData import PostData
from PostDatabase import Database
from flask import jsonify


app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

x = "hi"
ID = 0


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
    author = x
    comment = Comment(title, content, author, 0, ID)  # TODO figure out how to find parentID
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
    post = PostData(name, x, type, des, steps, ing, time, 0)
    print(" " + name + " " + x + " " + type + " " + des + " " + steps + " " + ing + " " + time)

    pst = Post()
    pst.pD = post
    pst.insertPost()
    pst.retrieveBrowsingPosts()
    recipes = pst.retrievedPosts
    print(len(recipes))

    return render_template("main-page.html", len=len(recipes), recipes=recipes)


@app.route('/view', methods=['POST'])
def view():
    postid = request.get_json()
    # print(postid)
    global ID
    ID = postid
    # return render_template("viewPost.html")
    resp = jsonify(success=True)
    return resp


@app.route('/viewPost', methods=['GET', 'POST'])
def viewPost():
    print(ID)
    pst = Post()
    pst.retrieveSinglePosts(ID)
    recipes = pst.retrievedPosts
    print(recipes[0].title)

    return render_template("viewPost.html", len=len(recipes), recipes=recipes)


if __name__ == "__main__":
    app.run()
