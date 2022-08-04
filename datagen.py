from datetime import date
import csv

head = ['itemname', 'price', 'date']
data = 'itemname,price,date'


def addEntry(itemname, price):
    global data
    data += f"\n{itemname},{price},{str(date.today())}"

    with open('test_tracker.csv', 'w') as file:
        writer = csv.writer(file)
        writer.writerow(head)
        writer.writerow([itemname, price, str(date.today())])


def getData():
    with open("test_tracker.csv") as file:
        csvData = csv.reader(file)
    return csvData


def testwrite():
    with open('test_tracker.csv', "w") as file:
        writer = csv.writer(file)
        writer.writerow(['hello', 'world'])

def initdata(worldname, customname):
    file = open(f'{worldname}_{customname}.csv', 'x')
    file.close()
