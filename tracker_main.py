from koreanParser import *
import datagen


def cmd(input: str):
    commands = parseCmd(input)
    if commands[0] == '초기화':
        datagen.initdata(commands[1], commands[2])
    else:
        datagen.addEntry(commands[0], parseNum(commands[1]))
