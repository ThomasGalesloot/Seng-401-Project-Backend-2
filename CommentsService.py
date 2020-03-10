
#comment creating
#comment posting
#upvote/downvote - arrayList - using count to get the amount
#hiding comments

#input is when we are called by the main program
#input is the event db, the most recent one
#output is nothing

#input is when we are called by the main process
#input is postID
#output is the comment


class CommentsService():

    def __init__(self, author, text, date, postID): #initializing the comment
        self.author = author    #author of the comment
        self.text = text    #text contained in the comment
        self.date = date    #date the comment was posted
        self.postID = postID    #post ID of the post the comment is parented to
        self.isUpvoted = False  #boolean true if the comment is upvoted
        self.isDownvoted = False    #boolean true if the comment is downvoted

    #TODO add a list of users who have upvoted and downvoted the comment
    def upvoteComment(self, postID, userID):
        if isUpvoted:
            self.upvoteCount -= 1   #remove the upvote
            self.isUpvoted = False  #remove the upvote
        if isDownvoted:
            self.upvoteCount += 2   #remove the downvote, add upvote
            self.isDownvoted = False    #remove the downvote, add upvote
            self.isUpvoted = True   #remove the downvote, add upvote


    def downvoteComment(self, postID, userID):
        if isUpvoted:
            self.upvoteCount += 2
            self.isDownvoted = False
            self.isUpvoted = True
        if isDownvoted:
            self.upvoteCount += 1
            self.isDownvoted = False

    def hideComment(self, postID):
        self.isHidden = True




