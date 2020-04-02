import json

from EventSourcingService.EventDatabase import EDatabase
from Event import Event
from CommentsDatabase import CommentsDatabase
from Comment import Comment

from flask import Flask, render_template, request, flash

from Comment import Comment
from flask import jsonify
from flask import Response

app = Flask(__name__)
# app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
app.config['SECRET_KEY'] = 'df^(*($#jfdkglI'

lastChecked = -1
ID = 1


@app.route("/fetchNew")
def updatecmtdb(self):
    commentsToAdd = Event.getnewevents(Event(0, 0), lastChecked)
    cdb = CommentsDatabase()
    for i in commentsToAdd:
        cdb.cursor.execute("INSERT INTO [dbo].[Comments] ("
                           "[postID]"
                           ",[userID]"
                           ",[votes]"
                           ",[cmtText]"
                           ",[cmtTitle])"
                           "VALUES"
                           "( " + str(i.parentPostID) +
                           ", '" + i.author +
                           "', " + str(0) +
                           ", '" + i.commentText +
                           "', '" + i.title + "')")
    self.lastChecked = Event.getnewid(Event(0, 0))
    return jsonify(success=True)


@app.route('/fetchCmts/<postid>')
def getCmts(postid):
    test = Comment()
    test.retrievedComments.clear()
    test.searchComment(postid)
    print("test")
    bigString = ""
    # temp = test.retrievedComments
    for x in range(0, len(test.retrievedComments)):
        bigString += " ((Title)) " + test.retrievedComments[x].title
        bigString += " ((Comment)) " + test.retrievedComments[x].commentText

    # return Response(json.dumps(test), mimetype='application/json')
    bigString2 = " " + str(len(test.retrievedComments)) + bigString + " "
    return jsonify(bigString2)


# http://127.0.0.1:5001/fetchCmts/{}

if __name__ == "__main__":
    app.run(port=5001)
