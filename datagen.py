from datetime import datetime
import csv
import pandas as pd

head = ['itemname', 'price', 'date']
dateformat = "%Y/%m/%d_%H:%M"
dataSet = 'default_tracker.csv'


def addEntry(itemname, price, time):
    with open(dataSet, 'a', encoding='utf-8-sig', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([itemname, price, str(
           time)])


def initdata(worldname, customname):
    file = open(f'{worldname}_{customname}.csv', 'x')
    writer = csv.writer(file)
    writer.writerow(head)
    file.close()


def setDataSet(name: str):
    global dataSet
    dataSet = name
    file = open(name, 'r')
    file.close()
