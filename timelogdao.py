from dbm import DatabaseManager
from datetime import date, datetime, time
import calendar
from timeent import TimeEntry
class TimeLogDAO:


    def __init__(self):
        self.dbm = DatabaseManager.get_instance()
        self.create_tables()



    def create_tables(self):
        self.dbm.execute('''  CREATE TABLE IF NOT EXISTS time_entries (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                date TEXT UNIQUE,
                clock_in TEXT,
                clock_out TEXT,
                duration REAL
            )
        '''
        )     


    def add_entry(self, date_str, clock_in_str):
        self.dbm.execute(
            'INSERT OR IGNORE INTO time_entries (date, clock_in, clock_out, duration) VALUES (?, ?, NULL, NULL)',
            (date_str, clock_in_str)
        )

    def update_entry(self, date_str, clock_out_str, duration):
        self.dbm.execute(
            'UPDATE time_entries SET clock_out=?, duration=? WHERE date=?',
            (clock_out_str, duration, date_str)
        )


    def get_entries_for_month(self, year, month):
        
        first = date(year, month, 1).isoformat()
        last_day = calendar.monthrange(year, month)[1]
        last = date(year, month, last_day).isoformat()


        
        cur = self.dbm.execute(
            'SELECT * FROM time_entries WHERE date BETWEEN ? AND ? ORDER BY date',
            (first, last)
        )        

        rows = cur.fetchall()

        entries = []

        for row in rows:
            entry = TimeEntry(
                entry_id=row['id'],
                date_str=row['date'],
                clock_in=row['clock_in'],
                clock_out=row['clock_out'],
                duration=row['duration'] or 0.0
            )
            entries.append(entry)

        return entries