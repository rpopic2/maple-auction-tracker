from sys import *
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

import pandas as pd
from pandas import DataFrame
import tracker_main
import datagen
import matplotlib.pyplot as plt

lastCommand = ''


def dummyOnEnter(e):
    onEnter()


def onEnter():
    global lastCommand
    lastCommand = mainEntry.get()
    if(lastCommand.startswith('지우기')):
        answer =  messagebox.askyesno('지우기', '정말로 가장 마지막에 입력한 정보를 지우시겠습니까?')
        if not answer:
            return
    elif(lastCommand == ''):
        print_welcome_screen()
        return
    try:
        result = tracker_main.cmd(lastCommand)
        if result is None:
            write("처리 성공")
            if lastCommand.startswith("불러오기"):
                print_welcome_screen()
        else:
            write(result)
    except Exception as err:
        write(f"처리 실패 : {err.args[0]}")
    plt.show()
    clearMainEntry()


def clearMainEntry(dummy=None):
    mainEntry.delete(0, "end")

def clfgraph(dummy=None):
    plt.clf()
    tracker_main.graph(tracker_main.lastViewdItem)
    plt.show()

def loadLastCmd(dummy):
    global lastCommand
    clearMainEntry(None)
    mainEntry.insert(0, lastCommand)


def write(message: str):
    outputLable.config(text=message)

def print_welcome_screen():
    statusbarLable.config(text=datagen.dataSet)
    df = tracker_main.getData()
    uniques = df.drop_duplicates(subset='itemname', keep='last')
    outputLable.config(text=f"{getHelpText}\n{uniques}")

getHelpText = "?를 입력하여 도움말 표시"

root = Tk()
root.title(f"메이플 옥션 트래커 v.{tracker_main.__version__}")
frm = ttk.Frame(root, padding=10)
frm.grid()

mainEntry = ttk.Entry(frm)
mainEntry.grid(row=0, column=0)

ttk.Button(frm, text="Enter", command=onEnter).grid(row=0, column=1)
root.bind("<Return>", dummyOnEnter)
root.bind("<Control-d>", exit)
root.bind("<Control-l>", clfgraph)
root.bind("<Up>", loadLastCmd)

statusbarLable = ttk.Label(frm)
statusbarLable.grid(row=2, column=0)
outputLable = ttk.Label(frm)
print_welcome_screen()

outputLable.grid(row=3, column=0)

plt.clf()
plt.show()
mainEntry.focus()

root.mainloop()
