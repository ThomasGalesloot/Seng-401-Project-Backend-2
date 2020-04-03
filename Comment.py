from CommentData import CommentData
from CommentsDatabase import CommentsDatabase
import json


class Comment:
    db = CommentsDatabase()
    retrievedComments = {}
    commentData = ""

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
                               "( " + str(
            self.commentData.parentPostID) +  # TODO make this get the post ID from the event table
                               ", '" + self.commentData.author +
                               "', " + str(0) +
                               ", '" + self.commentData.commentText +
                               "', '" + self.commentData.title + "')")
        print(str(self.parentPostID) + "\n\n\n")

        self.db.conn.commit()
        self.searchComment(self.parentPostID)

    def searchComment(self, toSearch):
        self.retrievedComments = {}
        self.db.cursor.execute(
            'select * from [dbo].[Comments] where postID =' + str(toSearch))
        for row in self.db.cursor.fetchall():
            temp = row[5]
            temp2 = row[4]
            self.retrievedComments[temp] = temp2

