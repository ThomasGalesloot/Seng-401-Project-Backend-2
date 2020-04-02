from datetime import datetime
from EventsDatabase import EventsDatabase

class Event:

    db = EventsDatabase()
    timeOccured = ""
    dateString = ""
    postID = ""
    # commentID = ""
    commentTitle = ""
    commentText = ""
    author = ""

    def __init__(self, pID, auth, cmtTitle, cmtText):
        # YYYY - MM - DD hh: mm:ss[.fractional seconds]
        self.timeOccurred = datetime(2013, 10, 31, 18, 23, 29, 227)
        self.dateString = self.timeOccured.strftime("%d/%m/%Y %H:%M:%S")
        # self.commentID = cID
        self.postID = pID
        self.commentText = cmtText
        self.commentTitle = cmtTitle
        self.author = auth


    def addEvent(self):
        print(
            "Title: " + self.title + "\nContent: " + self.commentText + "\nAuthor: " + self.author + + "\nPID: " + self.postID + "\nTimestamp: " + self.dateString)

        db = EventsDatabase()
        #  cd = CommentData("title", "commentText", "author", "votes", "parentPostID")
        # retrievedComments = []
        self.insertEvent()


    def insertEvent(self):

        # self.cd = CommentData("title", "commentText", "testing", "votes", "parentPostID")
        self.db.cursor.execute("INSERT INTO [dbo].[Events] ("
                               "[postID]"
                               ",[userID]"
                               ",[cmtText]"
                               ",[time]"
                               ",[cmtTitle])"
                               "VALUES"
                               "( " + str(self.parentPostID) +
                               ", '" + self.author +
                               "', '" + self.commentText +
                               "', '" + self.dateString +
                               "', '" + self.commentTitle + "')")
        print(str(self.parentPostID) + "\n\n\n")

        self.db.conn.commit()
        self.searchComment(self.parentPostID)
