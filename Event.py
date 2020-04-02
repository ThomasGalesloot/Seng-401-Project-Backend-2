from datetime import datetime
from time import strftime

from EventsDatabase import EventsDatabase
from CommentData import CommentData

class Event:
    eventID = ""
    CommentData = ""
    eventList = []

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
        self.timeOccurred = datetime.now()
        self.dateString = self.timeOccurred.strftime("%Y - %m - %d %H:%M:%S")
        print(self.dateString)
        # self.commentID = cID
        self.postID = pID
        self.commentText = cmtText
        self.commentTitle = cmtTitle
        self.author = auth


    def addEvent(self):
        print(
            "Title: " + self.commentTitle + "\nContent: " + self.commentText + "\nAuthor: " + self.author + "\nPID: " + str(self.postID) + "\nTimestamp: " + self.dateString)

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
                               "( " + str(self.postID) +
                               ", '" + self.author +
                               "', '" + self.commentText +
                               "', '" + self.dateString +
                               "', '" + self.commentTitle + "')")
        # print(str(self.parentPostID) + "\n\n\n")

        self.db.conn.commit()

    def getnewevents(self, lastid):
        self.db.cursor.execute(
            'select * from [dbo].[Events] where eventID >' + str(lastid))
        for row in self.db.cursor.fetchall():
            self.eventList.append(
                CommentData(row[6], row[1], row[2], row[3], 0, row[5]))
        return self.eventList

    def getnewid(self):
        self.db.cursor.execute(
            'select MAX(eventID) from [dbo].[Events]'
        )
        res = ""
        i: int
        for i in self.db.cursor.fetchall():
            res = i
        return res
