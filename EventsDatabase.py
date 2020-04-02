import pyodbc


class EventsDatabase:

    def __init__(self):
        self.conn = pyodbc.connect('Driver={SQL Server};'
                                   'Server=LAPTOP-7OES2EOP;'
                                   'Database=Events;'
                                   'Trusted_Connection=yes;')
        self.cursor = self.conn.cursor()