class CommentData:
    title = ""
    commentID = ""
    commentText = ""
    author = ""
    votes = ""
    parentPostID = ""

    def __init__(self, tit, cID, ppID, auth, votes, text):
        self.title = tit
        self.commentID = cID
        self.commentText = text
        self.votes = votes
        # self.datePosted = dp
        self.author = auth
        self.parentPostID = ppID

