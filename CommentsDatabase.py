import pyodbc


class CommentsDatabase:

    def __init__(self):
        self.conn = pyodbc.connect('Driver={SQL Server};'
                                   'Server=LAPTOP-2LU2E79L;'
                                   'Database=CommentsDatabase;'
                                   'Trusted_Connection=yes;')
        self.cursor = self.conn.cursor()