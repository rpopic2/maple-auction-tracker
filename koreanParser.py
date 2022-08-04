def parseNum(input: str) -> int:
    if ',' in input:
        input = input.replace(',', '')
    if '만' in input:
        i = input.index('만')
        n = float(input[:i])
        return n * 10000
    elif '.' in input:
        return parseNum(input + '만')
    else:
        return int(input)
