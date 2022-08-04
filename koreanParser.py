#utils
def parseNum(input: str) -> int:
    if ',' in input:
        input = input.replace(',', '')
    if '만' in input:
        return parseBigNums(input, '만', 4)
    elif '억' in input:
        return parseBigNums(input, '억', 8)
    elif '조' in input:
        return parseBigNums(input, '조', 12)
    elif '.' in input:
        return parseNum(input + '만')
    else:
        return int(input)

def parseBigNums(input, unit, e):
    i = input.index(unit)
    n = float(input[:i])
    return int(n * pow(10, e))

def parseCmd(input: str):
    return input.split(' ')
