class CommentData:
    postId = ""
    contents = ""
    datePosted = ""
    author = ""

    def __init__(self, pid, cont, dp, auth):
        self.postId = pid
        self.contents = cont
        self.datePosted = dp
        self.author = auth