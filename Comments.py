class Comments:

    title = ""
    content = ""

    def __init__(self, tit, cont):
        self.title = tit
        self.content = cont

    def addComment(self):
        print("Title: " + self.title + "\nContent: " + self.content)