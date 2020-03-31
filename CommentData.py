class CommentData:
    title = ""
    commentText = ""
    author = ""
    votes = ""
    parentPostID = ""

    def __init__(self, tit, text, auth, votes,  ppID):
        self.title = tit
        self.commentText = text
        self.votes = votes
        # self.datePosted = dp
        self.author = auth
        self.parentPostID = ppID

