import tkinter as tk
from tkinter import ttk, messagebox

from datetime import date, datetime


class ClockInOutFrame(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.ctrl = controller
        self._build()


    def _build(self):    
        self.pack(fill='both', expand=True)


        btn_in = tk.Button(self, text="Clock In", command=self._clock_in)
        btn_out = tk.Button(self, text="Clock Out", command=self._clock_out)
        self.status = tk.Label(self, text="Status: Not clocked in today")


        btn_in.pack(pady=10)
        btn_out.pack(pady=10)

        self.status.pack(pady=20)



    def _clock_in(self):
        try:
            self.ctrl.log_mgr.clock_in()
            self.refresh_status()
            self.ctrl.refresh_all()

        except Exception as e:
            messagebox.showerror("Error", str(e))



    def _clock_out(self):
        try:
            self.ctrl.log_mgr.clock_out()
            self.refresh_status()
            self.ctrl.refresh_all()
        except Exception as e:
            messagebox.showerror("Error", str(e))


    def refresh_status(self):
        today = date.today().isoformat()
        entries = self.ctrl.log_mgr.get_monthly_entries()


        for e in entries:
            if e.date == today and e.clock_in:
                if e.clock_out:
                    self.status.config(text=f"Today's work: {e.duration:.2f} h")
                else:
                    self.status.config(text=f"Clocked in at {e.clock_in}")
                return
            
        self.status.config(text="Status: Not clocked in today")






