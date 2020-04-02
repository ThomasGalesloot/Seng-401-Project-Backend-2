from CommentData import CommentData
from CommentsDatabase import CommentsDatabase
import json


class Comment:
    db = CommentsDatabase()
    title = ""
    commentText = ""
    author = ""
    votes = ""
    parentPostID = ""
    retrievedComments = []

    def __init__(self, tit, cont, auth, votes, parentPostID):
        self.title = tit
        self.commentText = cont
        self.author = auth
        self.votes = 0
        self.parentPostID = parentPostID

    def addComment(self):
        print(
            "Title: " + self.title + "\nContent: " + self.commentText + "\nAuthor: " + self.author)

        db = CommentsDatabase()
        #  cd = CommentData("title", "commentText", "author", "votes", "parentPostID")
        # retrievedComments = []
        self.insertComment()

    # inserts a brand new comment into the db
    def insertComment(self):

        # self.cd = CommentData("title", "commentText", "testing", "votes", "parentPostID")
        self.db.cursor.execute("INSERT INTO [dbo].[Comments] ("
                               "[postID]"
                               ",[userID]"
                               ",[votes]"
                               ",[cmtText]"
                               ",[cmtTitle])"
                               "VALUES"
                               "( " + str(self.parentPostID) +  # TODO make this get the post ID from the event table
                               ", '" + self.author +
                               "', " + str(0) +
                               ", '" + self.commentText +
                               "', '" + self.title + "')")
        print(str(self.parentPostID) + "\n\n\n")

        self.db.conn.commit()
        self.searchComment(self.parentPostID)

    def searchComment(self, toSearch):
        self.db.cursor.execute(
            'select * from [dbo].[Comments] where postID =' + str(toSearch))
        for row in self.db.cursor.fetchall():
            self.retrievedComments.append(
                CommentData(row[5], row[0], row[1], row[2], row[3], row[4]))



