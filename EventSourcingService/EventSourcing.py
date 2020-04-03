import json
from json.decoder import JSONArray

import jsonpickle

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



@app.route("/fetchNew")
def updatecmtdb():
    eventcontroller = Event()
    lastID = eventcontroller.getLastChecked()
    commentsToAdd = eventcontroller.getnewevents(lastID)
    cdb = CommentsDatabase()
    for i in commentsToAdd:
        print("fck")
        cdb.cursor.execute("INSERT INTO CommentsDatabase.dbo.Comments ("
                               "[postID]"
                               ",[userID]"
                               ",[votes]"
                               ",[cmtText]"
                               ",[cmtTitle])"
                               "VALUES"
                               "( " + str(i.postID) +
                               ", '" + i.author +
                               "', " + str(0) +
                               ", '" + i.commentText +
                               "', '" + i.commentTitle + "')")
        cdb.conn.commit()
    print("sucks")
    newID = eventcontroller.getnewid()
    eventcontroller.updateLastChecked(newID)
    commentsToAdd.clear()
    return "sucess!"


@app.route('/fetchCmts/<postid>')
def getCmts(postid):
    test = Comment()
    test.searchComment(postid)
    return jsonify(test.retrievedComments)
    # return jsonify(test.retrievedComments)
# http://127.0.0.1:5001/fetchCmts/{}

if __name__ == "__main__":
    app.run(port=5001)
