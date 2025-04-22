import tkinter as tk

class SummaryFrame(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.ctrl = controller
        self._build()


    def _build(self):
        self.pack(fill='both', expand=True)

        self.lbl_total = tk.Label(self, text="")
        self.lbl_remain = tk.Label(self, text="")
        self.lbl_days = tk.Label(self, text="")
        self.lbl_target = tk.Label(self, text="")


        self.lbl_total.pack(pady=10)
        self.lbl_remain.pack(pady=10)
        self.lbl_days.pack(pady=10)
        self.lbl_target.pack(pady=10)



    def refresh(self):
        entries = self.ctrl.log_mgr.get_monthly_entries()
        total = self.ctrl.log_mgr.total_hours(entries)
        remain = self.ctrl.scheduler.hours_remaining(70, total)
        days = self.ctrl.scheduler.days_remaining()
        target = self.ctrl.scheduler.daily_target(remain, days)
        self.lbl_total.config(text=f"Total hours worked: {total}")
        self.lbl_remain.config(text=f"Hours remaining to 70 h: {remain}")
        self.lbl_days.config(text=f"Days left in month: {days}")
        self.lbl_target.config(text=f"Need to work {target} h/day")