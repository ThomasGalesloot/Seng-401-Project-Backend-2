from CommentData import CommentData
from CommentsDatabase import CommentsDatabase


class Comment:
    db = CommentsDatabase()
    title = ""
    commentText = ""
    author = ""
    votes = ""
    parentPostID = ""

    def __init__(self, tit, cont, auth, votes, parentPostID):
        self.title = tit
        self.commentText = cont
        self.author = auth
        self.votes = 0
        self.parentPostID = 0

    def addComment(self):
        print(
            "Title: " + self.title + "\nContent: " + self.commentText + "\nAuthor: " + self.author)

        db = CommentsDatabase()
        #  cd = CommentData("title", "commentText", "author", "votes", "parentPostID")
        retrievedComments = []
        self.insertComment()

    # inserts a brand new comment into the db
    def insertComment(self):

        # self.cd = CommentData("title", "commentText", "testing", "votes", "parentPostID")
        self.db.cursor.execute("INSERT INTO [dbo].[Comments] ("
                                   "[postID]"
                                   ",[userID]"
                                   ",[votes]"
                                   ",[cmtText])"
                                   "VALUES"
                                   "( " + str(self.parentPostID) + # TODO make this get the post ID from the event table, also why does this need to be string, also removed ''
                                    ", '" + self.author +
                                    "', " + str(0) +
                                    ", '" + self.commentText + "')")

        self.db.conn.commit()
