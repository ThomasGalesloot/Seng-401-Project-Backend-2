from Database import Database
from PostData import PostData


class Search:
    db = Database()
    retrievedPost = []

    # Will search posts based on title alone
    def searchPostsByTitle(self, searchQuery):
        self.db.cursor.execute('select * from Project.dbo.posts_info where Title like \'%' + searchQuery + "%\'")
        allPosts = self.db.cursor.fetchall()
        for row in allPosts:
            if row[2] is not None and row[3] is not None:
                self.retrievedPost.append(PostData(row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[0]))

    # Will search posts by type alone
    def searchPostsByType(self, searchQuery):
        self.db.cursor.execute('select * from Project.dbo.posts_info where Type =' + searchQuery)
        allPosts = self.db.cursor.fetchall()
        for row in allPosts:
            if row[2] is not None and row[3] is not None:
                self.retrievedPosts.append(PostData(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]))
