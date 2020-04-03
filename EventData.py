from datetime import datetime

class EventData:
    timeOccured = ""
    dateString = ""
    postID = ""
    # commentID = ""
    commentTitle = ""
    commentText = ""
    author = ""
    eventID = ""

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