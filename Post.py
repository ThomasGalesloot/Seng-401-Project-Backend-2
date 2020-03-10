from Database import Database
from PostData import PostData


class Post:
    db = Database()

   #inserts a brand new post into the db
    def insertPost(self):
        # retrieve some value here to fill PostData
        # placeholder for now below, remove once uneeded
        pD = PostData(1, "Title", "Owner", "Type", "Description", "Steps", "Ingredients", 3)
        self.db.cursor.execute("INSERT INTO [dbo].[post_info] ("
            "[Id]"
            ",[Title]"
            ",[Owner]"
            ",[Type]"
            ",[Description] "
            ",[Steps]"
            ",[Ingredients]"
            ",[Prep_Time])"
            "VALUES"
            "(<Id," + pD.id + ",>"
            ",<Title," + pD.title + ",>"
            ",<Owner," + pD.owner + ",>"
            ",<Type," + pD.type + ",>"
            ",<Description," + pD.description + ",>"
            ",<Steps," + pD.steps + ",>"
            ",<Ingredients," + pD.ingredients + ",>"
           ",<Prep_Time," + pD.prep_Time + ",>)")
        self.db.commit()

    # retrieves posts for browsing on the DB on the db
    def retrieveBrowsingPosts(self):
        self.db.cursor.execute('select Title, Owner, Type from Users.dbo.login_info')
        allPosts = self.db.cursor.fetchall()
        retrievedPosts = []
        for row in allPosts:
            retrievedPosts.append(PostData(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]))

    # retrieves a single post allowing it to be posted
    def retrieveSinglePostPage(self):
        # We should probably create a different data store type that has the ability to only grab title and owner and
        # return a full PostData object
        pD = PostData(1, "Title", "Owner", "Type", "Description", "Steps", "Ingredients", 3)
        self.db.cursor.execute('select * from Users.dbo.login_info where Title =' + pD.title + 'and Owner = ' + pD.owner )
        allPosts = self.db.cursor.fetchall()
        retrievedPosts = []
        for row in allPosts:
            retrievedPosts.append(PostData(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]))