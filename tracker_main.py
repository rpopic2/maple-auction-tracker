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
lastEnteredItem = None

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
            datagen.initdata(commands[1], commands[2])
        case '불러오기':
            datagen.setDataSet(commands)
        case '열기':
            os.startfile(datagen.dataSet)
        case '보기':
            return view(commands)
        case '그래프':
            return graphcmd(commands)
        case _:
            return register(commands)


def showHelp():
    result = f"메이플 옥션 트래커 v.{__version__} by 스카니아 seauma"
    file = open('help.txt', encoding='utf-8-sig')
    data = file.read()
    file.close()
    return result + data


def register(commands):
    if len(commands) != 1:
        global lastEnteredItem
        global lastViewdItem
        lastEnteredItem = commands[0]
        lastViewdItem = commands[0]
    if len(commands) != 3:
        commands.append(datetime.now().strftime(datagen.dateformat))
    elif len(commands) == 3:
        commands[2] = parser.parse(commands[2]).strftime(datagen.dateformat)
    datagen.addEntry(lastEnteredItem, parseNum(commands[1]), commands[2])
    return view_singleItem(getData(), lastEnteredItem)


def view(commands):
    df = getData()
    if len(commands) == 1:
        return df
    else:
        global lastViewdItem
        lastViewdItem = commands[1]
        return df.loc[df['itemname'] == commands[1]]

def view_singleItem(df, itemname):
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
