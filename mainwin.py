import tkinter as tk
from tkinter import ttk, messagebox

from clock import ClockInOutFrame
from entries import EntriesFrame
from summary import SummaryFrame


from timelogmanager import TimeLogManager
from scheduler import Scheduler





class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Work Hour Scheduler")
        self.geometry("600x400")


        self.log_mgr = TimeLogManager()
        self.scheduler = Scheduler()



        self._build_ui()



    def refresh_all(self):
        self.entries_frame.refresh()
        self.summary_frame.refresh()





    def _build_ui(self):
        tab_control = ttk.Notebook(self)    
        self.clock_frame = ClockInOutFrame(tab_control, self)
        self.entries_frame = EntriesFrame(tab_control, self)
        self.summary_frame = SummaryFrame(tab_control, self)



        tab_control.add(self.clock_frame, text="Clock In/Out")
        tab_control.add(self.entries_frame, text="Entries")
        tab_control.add(self.summary_frame, text="Summary")

        tab_control.pack(expand=1, fill="both")






    def count(self):
        cnt= 2+7
    
        return cnt