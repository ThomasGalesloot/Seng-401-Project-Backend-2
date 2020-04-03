from MainApplication.PostDatabase import Database


class Login:
    username = ""
    password = ""
    db = Database()
    confirm_found = "false"

    def __init__(self, na, pa):
        self.username = na
        self.password = pa

    def compare(self):
        rowcount = self.db.cursor.execute('select * from Project.dbo.login_info WHERE username =? AND password = ?',
                                          (self.username, self.password))

        rows = rowcount.fetchone()
        if rows is None:
            self.confirm_found = "false"
        else:
            self.confirm_found = "true"



