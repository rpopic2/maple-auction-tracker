from datetime import datetime
import csv
from http import server
import pandas as pd

head = ['itemname', 'price', 'date']
dateformat = "%Y/%m/%d_%H:%M"
dataSet = 'default_0.csv'


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


def setDataSet(servername, index):
    global dataSet
    dataSet = f"{servername}_{index}.csv"
    file = open(dataSet, 'r')
    file.close()
    with open('options', 'w', encoding='utf-8-sig') as file:
        file.write(dataSet)
