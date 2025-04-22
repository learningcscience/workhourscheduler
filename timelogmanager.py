from timelogdao import TimeLogDAO
from datetime import date, datetime, time

class TimeLogManager:
    def __init__(self):
        self.dao = TimeLogDAO()



    def clock_in(self):
        today = date.today().isoformat()
        now = datetime.now().time().isoformat(timespec='seconds')

        self.dao.add_entry(today, now)



    def clock_out(self):
        today = date.today().isoformat()
        now = datetime.now().time()

        #fetch existing entry
        entries = self.dao.get_entries_for_month(date.today().year, date.today().month)

        for e in entries:
            if e.date == today and e.clock_in:
                ci = datetime.strptime(e.clock_in, '%H:%M:%S').time()


                #duration calculate
                dt_ci = datetime.combine(date.today(), ci)
                dt_co = datetime.combine(date.today(), now)

                duration = (dt_co - dt_ci).total_seconds() / 3600
                self.dao.update_entry(today, now.isoformat(timespec='seconds'), duration)
                return

        raise ValueError("No clock-in entry found for today. Please clock in first.")
    


    def get_monthly_entries(self):
        today = date.today()
        return self.dao.get_entries_for_month(today.year, today.month)


    def total_hours(self, entries):
        total = 0.0
        for entry in entries:
            if entry.duration:
                total += entry.duration
        return total
    

    
