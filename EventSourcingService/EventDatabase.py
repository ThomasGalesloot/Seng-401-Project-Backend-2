import pyodbc


class EDatabase:

    def __init__(self):
        self.conn = pyodbc.connect('Driver={SQL Server};'
                                   'Server=LAPTOP-3VMNV60Q;'
                                   'Database=Events;'
                                   'Trusted_Connection=yes;')
        self.cursor = self.conn.cursor()
