from tkinter import *
from tkinter import ttk

root = Tk()
root.title("메이플 옥션 트래커")
frm = ttk.Frame(root, padding=10)
frm.grid()

ttk.Entry(frm).grid(column=0, row= 0)
ttk.Label(frm, text="안녕").grid(column=0, row=2)
ttk.Button(frm, text="Enter", command=None).grid(column=1, row=0)


ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=1)

root.mainloop()