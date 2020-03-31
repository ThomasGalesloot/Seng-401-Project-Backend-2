from PostDatabase import Database
from PostData import PostData


class Search:
    db = Database()


    def searchPostsByTitle(self, searchquerry):
        self.db.cursor.execute('select * from Users.dbo.login_info where Title LIKE %' + searchquerry + '%')
        allPosts = self.db.cursor.fetchall()
        retrievedPosts = []
        for row in allPosts:
            if row[2] is not None and row[3] is not None:
                retrievedPosts.append(PostData(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]))

    def searchPostsByType(self, searchquerry):
        self.db.cursor.execute('select * from Users.dbo.login_info where Type =' + searchquerry)
        allPosts = self.db.cursor.fetchall()
        retrievedPosts = []
        for row in allPosts:
            if row[2] is not None and row[3] is not None:
                retrievedPosts.append(PostData(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]))


