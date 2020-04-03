import pyodbc


class EventsDatabase:

    def __init__(self):
        self.conn = pyodbc.connect('Driver={SQL Server};'
                                   'Server=LAPTOP-2LU2E79L;'
                                   'Database=EventsDatabase;'
                                   'Trusted_Connection=yes;')
        self.cursor = self.conn.cursor()