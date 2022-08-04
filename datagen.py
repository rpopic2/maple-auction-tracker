from datetime import datetime
import csv
import pandas as pd

head = ['itemname', 'price', 'date']
dateformat = "%Y/%m/%d_%H:%M"


def addEntry(itemname, price):
    with open('test_tracker.csv', 'a', encoding='utf-8-sig', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([itemname, price, str(
            datetime.now().strftime(dateformat))])


def getData():
    return pd.read_csv('test_tracker.csv')


def initdata(worldname, customname):
    file = open(f'{worldname}_{customname}.csv', 'x')
    writer = csv.write(file)
    writer.writerow(head)
    file.close()
