import pyodbc


class CommentsDatabase:

    def __init__(self):
        self.conn = pyodbc.connect('Driver={SQL Server};'
                                   'Server=LAPTOP-3VMNV60Q;'
                                   'Database=CommentsDatabase;'
                                   'Trusted_Connection=yes;')
        self.cursor = self.conn.cursor()