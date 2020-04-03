import pyodbc


class EDatabase:

    def __init__(self):
        self.conn = pyodbc.connect('Driver={SQL Server};'
                                   'Server=DESKTOP-Q5ABK7U;'
                                   'Database=EventsDatabase;'
                                   'Trusted_Connection=yes;')
        self.cursor = self.conn.cursor()
