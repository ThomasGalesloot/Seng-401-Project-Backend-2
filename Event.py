class Event:

    timeOccurred = ""
    eventType = ""
    commentID = ""

    def __init__(self, time, type, cmt):
        self.timeOccurred = time
        self.eventType = type
        self.commentID = cmt
