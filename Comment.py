from CommentData import CommentData
from CommentsDatabase import CommentsDatabase


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
        self.parentPostID = 0

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
                               ",[cmtText])"
                               "VALUES"
                               "( " + str(self.parentPostID) +  # TODO make this get the post ID from the event table
                               ", '" + self.author +
                               "', " + str(0) +
                               ", '" + self.commentText + "')")

        self.db.conn.commit()
        self.searchComment(0)

    def searchComment(self, toSearch):
        self.db.cursor.execute(
            'select * from [dbo].[Comments] where postID =' + str(0))  #TODO replace 0 with toSearch when done testing
        for row in self.db.cursor.fetchall():
            self.retrievedComments.append(
                CommentData("title", row[0], row[1], row[2], row[3], row[4]))  # TODO add title to db and implement
        for i in self.retrievedComments:
            print(i.title + "," + i.commentText + "," +
                  i.author + "," + str(i.votes) + "," +
                  str(i.parentPostID) + "\n")  # May need to put votes and ids in str()

