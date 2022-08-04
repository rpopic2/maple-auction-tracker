from koreanParser import *
import datagen


def cmd(input: str):
    commands = parseCmd(input)
    datagen.addEntry(commands[0], parseNum(commands[1]))
