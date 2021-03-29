symbolLookup = [
    ['I', 'V', 'X'],
    ['X', 'L', 'C'],
    ['C', 'D', 'M'],
    ['_I', '_V', '_X'],
    ['_X', '_L', '_C'],
    ['_C', '_D', '_M'],
]

valueLookup = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000,

    '_I': 1000,
    '_V': 5000,
    '_X': 10000,
    '_L': 50000,
    '_C': 100000,
    '_D': 500000,
    '_M': 1000000,
}


def convertFromInt(input: int) -> str:
    result: str = ''
    idx: int = 0
    i = input
    while True:
        if i == 0:
            break;

        r: int = i % 10
        cur: str = result

        result = ''
        if 1 <= r <= 3:
            result = ''.join([symbolLookup[idx][0] for c in range(r)])
        elif r == 4:
            result = (symbolLookup[idx][0] + symbolLookup[idx][1])
        elif r == 5:
            result = symbolLookup[idx][1]
        elif 6 <= r <= 8:
            result = symbolLookup[idx][1] + ''.join([symbolLookup[idx][0] for c in range(r - 5)])
        elif r == 9:
            result = (symbolLookup[idx][0] + symbolLookup[idx][2])

        result += cur
        i = int(i / 10)
        idx += 1
        #print(f'i = {i}, r = {r},  idx = {idx}, *** result *** = {result}')
    return result


def getRomanValue (t: str) -> int:
    return  valueLookup[t]


def convertToInt(input: str) -> int:
    result: int = 0
    prev: int = -1

    if not  input:
        return result

    token : str = ''
    for c in input:
        token += c
        if c != '_':
            cur: int = getRomanValue (token)
            if cur > prev > 0:
                result -= (prev + prev)
            result += cur
            token = ''
            prev = cur

    return result


if __name__ == "__main__":
    print(symbolLookup)
    while True:
        v : int = int(input())
        result : str = convertFromInt(v)
        print (f' Roman = {result} ' )

        i :int = convertToInt (result)
        print(f' Int = {i} ')

