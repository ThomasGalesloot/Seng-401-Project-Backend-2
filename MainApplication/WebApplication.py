from flask import Flask, render_template, request, flash

from MainApplication.Event import Event
from MainApplication.EventData import EventData
from MainApplication.Login import Login
from MainApplication.Post import Post
from MainApplication.PostData import PostData
from flask import jsonify
import requests
from MainApplication.Search import Search


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
    if Test.confirm_found == "true":
        pst = Post()
        pst.retrieveBrowsingPosts()
        recipes = pst.retrievedPosts

        return render_template("main-page.html", len=len(recipes), recipes=recipes)
    else:
        flash('Invalid Credentials, please try again')
        return render_template("profile.html")


@app.route('/comment', methods=['POST'])
def comment():
    postid = request.get_json()
    global ID
    ID = postid
    # return render_template("viewPost.html")
    resp = jsonify(success=True)
    return resp


@app.route('/commentPost', methods=['POST'])
def postComment():
    title = request.form['title']
    content = request.form['content']
    author = x
    pst = Post()
    pst.retrieveBrowsingPosts()
    recipes = pst.retrievedPosts
    event = EventData(ID, x, title, content)
    eventcontroller = Event()
    eventcontroller.addEvent(event)

    try:
        ping = requests.get("http://127.0.0.1:5001//fetchNew")
    except requests.exceptions.ConnectionError:
        return render_template("viewPost.html", len=len(recipes), recipes=recipes)
    c = []
    t = []
    leng = 0
    try:
        req = requests.get("http://127.0.0.1:5001/fetchCmts/{}".format(ID))
    except requests.exceptions.ConnectionError:
        return render_template("viewPost.html", len=len(recipes), recipes=recipes, leng=leng, c=c, t=t)
    thecomments = req.json()
    leng = len(thecomments)
    t = list(thecomments.keys())
    c = list(thecomments.values())


    return render_template("viewPost.html", len=len(recipes), recipes=recipes, leng=leng, c=c, t=t)




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

    pst = Post()
    pst.pD = post
    pst.insertPost()
    pst.retrieveBrowsingPosts()
    recipes = pst.retrievedPosts

    return render_template("main-page.html", len=len(recipes), recipes=recipes)


@app.route('/view', methods=['POST'])
def view():
    postid = request.get_json()
    global ID
    ID = postid
    # return render_template("viewPost.html")
    resp = jsonify(success=True)
    return resp


@app.route('/viewPost', methods=['GET', 'POST'])
def viewPost():
    pst = Post()
    pst.retrieveSinglePosts(ID)
    recipes = pst.retrievedPosts
    c = []
    t = []
    leng = 0
    try:
        req = requests.get("http://127.0.0.1:5001/fetchCmts/{}".format(ID))
    except requests.exceptions.ConnectionError:
        return render_template("viewPost.html", len=len(recipes), recipes=recipes, leng=leng, c=c, t=t)
    thecomments = req.json()
    leng = len(thecomments)
    t = list(thecomments.keys())
    c = list(thecomments.values())



    return render_template("viewPost.html", len=len(recipes), recipes=recipes, leng=leng, c=c, t=t)


@app.route('/mainPage', methods=['POST'])
def mainPage():
    pst = Post()
    pst.retrieveBrowsingPosts()
    recipes = pst.retrievedPosts

    return render_template("main-page.html", len=len(recipes), recipes=recipes)


@app.route('/search', methods=['POST'])
def search():
    search = request.form['inSearch']
    ser = Search()
    ser.retrievedPost.clear()
    ser.searchPostsByTitle(search)
    recipes = ser.retrievedPost

    return render_template("main-page.html", len=len(recipes), recipes=recipes)


if __name__ == "__main__":
    app.run()
