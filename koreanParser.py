# utils

from ast import parse


unitdict = {
    '십': 1,
    '백': 2,
    '천': 3,
    '만': 4,
    '억': 8,
    '조': 12,
}
units = unitdict.keys()


def parseNum(input: str) -> int:
    if ',' in input:
        input = input.replace(',', '')
    for c in input:
        if c in unitdict:
            return parseBigNums(input, c, unitdict[c])
    return int(input)


def parseBigNums(input, unit, exponential):
    i = input.index(unit)
    n = float(input[:i])
    return int(n * pow(10, exponential))


def parseCmd(input: str):
    return input.split(' ')
