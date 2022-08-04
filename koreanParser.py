def parseNum(input: str) -> int:
    if ',' in input:
        input = input.replace(',', '')
    if '만' in input:
        i = input.index('만')
        n = float(input[:i])
        return int(n * 10000)
    elif '억' in input:
        i = input.index('억')
        n =float(input[:i])
        return int(n * 100000000)
    elif '.' in input:
        return parseNum(input + '만')
    else:
        return int(input)

def parseCmd(input:str):
    return input.split(' ')
