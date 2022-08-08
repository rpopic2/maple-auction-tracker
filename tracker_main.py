from os.path import exists
import os
from dateutil import parser
from datetime import datetime
from koreanParser import *
import datagen
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas as pd

lastViewdItem = None

if not exists("options"):
    with open("options", 'x', encoding='utf-8-sig') as f:
        f.write(datagen.dataSet)

with open("options", encoding='utf-8-sig') as file:
    datagen.dataSet = file.read()

if not exists(datagen.dataSet):
    datagen.initdata('default', '0')

__version__ = 1.1


def cmd(input: str):
    commands = parseCmd(input)
    match commands[0]:
        case '?':
            return showHelp()
        case '버전':
            return __version__
        case '새파일':
            datagen.initdata(commands[1])
        case '불러오기':
            datagen.setDataSet(commands[1])
        case '열기':
            os.startfile(datagen.dataSet)
        case '전체':
            return view_all(commands)
        case '그래프지우기':
            clfgraph()
        case '지우기':
            cancel_df = getData().iloc[:-1]
            cancel_df.to_csv(datagen.dataSet, index=False)
            return getData()
        case _:
            try:
                num = parseNum(commands[0])
                return registerCmd(commands)
            except Exception as e:
                if len(commands) != 1:#on additional numbers input
                    global lastViewdItem
                    lastViewdItem = commands[0]
                    return registerCmd(commands[1:])
                return view_singleItem(getData(), commands[0])
            
def registerCmd(commands):
    if len(commands) == 1:
        commands.append(None)
    return register(lastViewdItem, commands[0], commands[1])

def clfgraph():
    plt.clf()
    plt.show()

def showHelp():
    result = f"메이플 옥션 트래커 v.{__version__} by 스카니아 seauma"
    with open('help.txt', encoding='utf-8-sig') as file:
        data = file.read()
    return result + data


def register(itemname, price, time=None):
    if time is None:
        time = datetime.now().strftime(datagen.dateformat)
    else:
        time = parser.parse(time).strftime(datagen.dateformat)
    datagen.addEntry(itemname, parseNum(price), time)
    return view_singleItem(getData(), itemname)


def view_all(commands):
    df = getData()
    if len(commands) == 1:
        return df


def view_singleItem(df, itemname):
    global lastViewdItem
    lastViewdItem = itemname
    graph(itemname)
    return df.loc[df['itemname'] == itemname]


def getData():
    return pd.read_csv(datagen.dataSet)


def graphcmd(commands):
    if len(commands) != 1:
        global lastViewdItem
        lastViewdItem = commands[1]
    return graph(lastViewdItem)


def graph(itemname):
    df = getbyname(itemname)
    df['date'] = pd.to_datetime(df['date'], format=datagen.dateformat)
    df = df.sort_values(by='date')
    plt.plot(df['date'], df['price'])
    return df


def getbyname(itemname):
    df = getData()
    return df.loc[df['itemname'] == itemname]
