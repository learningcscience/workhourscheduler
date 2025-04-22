import tkinter as tk
from tkinter import ttk, messagebox

class EntriesFrame(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.ctrl = controller
        self._build()


    def _build(self):
        self.pack(fill='both', expand=True)

        cols = ('Date', 'In', 'Out', 'Duration')

        self.tree = ttk.Treeview(self, columns=cols, show='headings')


        for c in cols:
            self.tree.heading(c, text=c)


        self.tree.pack(fill='both', expand=True, padx=10, pady=10)


        btn = tk.Button(self, text="Refresh", command=self.refresh)

        btn.pack(pady=10)
    


    def refresh(self):
        for row in self.tree.get_children():
            self.tree.delete(row)

        entries = self.ctrl.log_mgr.get_monthly_entries()

        for e in entries:
            self.tree.insert('', 'end', values=(e.date, e.clock_in or '', e.clock_out or '', f"{e.duration:.2f}"))            
