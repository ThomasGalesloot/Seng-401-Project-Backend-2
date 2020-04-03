from datetime import datetime
from time import strftime

from EventData import EventData
from EventsDatabase import EventsDatabase
from CommentData import CommentData


class Event:

    eventData = ""
    eventList = []

    db = EventsDatabase()


    def addEvent(self, EventData):
        self.eventData =EventData

        db = EventsDatabase()
        #  cd = CommentData("title", "commentText", "author", "votes", "parentPostID")
        # retrievedComments = []
        self.insertEvent()

    def insertEvent(self):

        self.db.cursor.execute("INSERT INTO [dbo].[Events] ("
                               "[postID]"
                               ",[userID]"
                               ",[cmtText]"
                               ",[datePosted]"
                               ",[cmtTitle])"
                               "VALUES"
                               "( " + str(self.eventData.postID) +
                               ", '" + self.eventData.author +
                               "', '" + self.eventData.commentText +
                               "', '" + self.eventData.dateString +
                               "', '" + self.eventData.commentTitle + "')")
        # print(str(self.parentPostID) + "\n\n\n")

        self.db.conn.commit()

    def getnewevents(self, lastid):
        self.db.cursor.execute(
            'select * from EventsDatabase.dbo.Events where eventID >' + str(lastid[0][0]))
        for row in self.db.cursor.fetchall():
            self.eventList.append(
                EventData(row[1], row[2], row[5], row[3]))
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


    def getLastChecked(self):
        self.db.cursor.execute('select * from EventsDatabase.dbo.NewCount')
        return self.db.cursor.fetchall()

    def updateLastChecked(self, new_val):
        self.db.cursor.execute('UPDATE EventsDatabase.dbo.NewCount SET newestEventID = ' + str(new_val[0]))
        self.db.conn.commit()
