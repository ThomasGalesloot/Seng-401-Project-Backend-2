from EventSourcingService.EventDatabase import EDatabase
from CommentData import CommentData


class Event:
    eventID = ""
    CommentData = ""
    time = ""
    db = EDatabase()
    eventList = []

    def __init__(self, time, cmt):
        self.time = time
        self.commentID = cmt

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
