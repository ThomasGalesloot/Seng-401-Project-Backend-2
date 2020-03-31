from Database import Database
from PostData import PostData


class Post:
    db = Database()
    retrievedPosts = []

    # inserts a brand new post into the db
    def insertPost(self):
        # retrieve some value here to fill PostData
        # placeholder for now below, remove once unneeded
        self.db.cursor.execute("INSERT INTO [dbo].[posts_info]"
                               "([Title]"
                               ",[Owner]"
                               ",[Type]"
                               ",[Description]"
                               ",[Steps]"
                               ",[Ingredients]"
                               ",[Prep_Time])"
                               "VALUES"
                               "( '" + self.pD.title
                               + "', '" + self.pD.owner
                               + "', '" + self.pD.type
                               + "','" + self.pD.description
                               + "','" + self.pD.steps
                               + "', '" + self.pD.ingredients
                               + "', '" + self.pD.prep_Time + "')")

        self.db.conn.commit()

    # retrieves posts for browsing on the DB on the db
    def retrieveBrowsingPosts(self):
        self.db.cursor.execute('select * from posts_info')
        self.retrievedPosts = []
        i = 0
        for row in self.db.cursor.fetchall():
            self.retrievedPosts.append(PostData( row[1], row[2], row[3], row[4], row[5], row[6], row[7],row[0]))

    # retrieves a single post allowing it to be posted
    def retrieveSinglePostPage(self):
        # We should probably create a different data store type that has the ability to only grab title and owner and
        # return a full PostData object
        pD = PostData("Title", "Owner", "Type", "Description", "Steps", "Ingredients", 3)
        self.db.cursor.execute(
            'select * from Project.dbo.login_info where Title =' + pD.title + 'and Owner = ' + pD.owner)
        allPosts = self.db.cursor.fetchall()
        retrievedPosts = []
        for row in allPosts:
            self.retrievedPosts.append(PostData(row[1], row[2], row[3], row[4], row[5], row[6], row[7]))
