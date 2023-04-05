STDCONST = {
    'KOR_FIRST' : ord('가'),
    'KOR_LAST' : ord('힣'),
    'BLANK' : ord(' '),
    'EN_LOWER_FIRST' : ord('a'),
    'EN_LOWER_LAST' : ord('z'),
    'EN_UPPER_FIRST' : ord('A'),
    'EN_UPPER_LAST' : ord('Z'),
    'NUM_FIRST' : ord('0'),
    'NUM_LAST' : ord('9')
}

def int_n(n, q):
    rev_base = ''

    while n > 0:
        n, mod = divmod(n, q)
        rev_base += str(mod)

    return rev_base[::-1] 

def binToUga(charBin):
    charBin = charBin.replace('0', '우')
    charBin = charBin.replace('1', '가')
    return charBin

def korToUga(char):
    """
    '가' -> '우우 ... 우우' (16)
    '갸' -> '우우 ... 우가' (16)
    ...
    '힣' -> '가가 ... 가가' (16)
    """
    result = ''
    charNum = ord(char) - STDCONST['KOR_FIRST']
    charBin = bin(charNum)[2:].zfill(16)
    result = binToUga(charBin)
    return result

def enToUga(char, isUpper):
    """
    'A' -> '가우우우우우' (6)
            ^^ : Upper
    'a' -> '우우우우우우' (6)
            ^^ : Lower
    """
    result = ''
    charNum = ord(char)
    if isUpper:
        charNum -= STDCONST['EN_UPPER_FIRST']
        result += '가'
    elif not isUpper:
        charNum -= STDCONST['EN_LOWER_FIRST']
        result += '우'
    charBin = bin(charNum)[2:].zfill(5)
    result += binToUga(charBin)
    return result

def numToUga(char):
    """
    '0' -> '우우우우' (4)
    ...
    '9' -> '가우가우' (4)
    """
    charNum = ord(char) - STDCONST['NUM_FIRST']
    charBin = bin(charNum)[2:].zfill(4)
    result = binToUga(charBin)
    return result

def textToUga(text):
    result = ''
    for char in text:
        charNum = ord(char)
        if charNum == STDCONST['BLANK']:
            result += '우가'
        elif charNum >= STDCONST['KOR_FIRST'] and charNum <= STDCONST['KOR_LAST']:
            result += korToUga(char)
        elif charNum >= STDCONST['EN_LOWER_FIRST'] and charNum <= STDCONST['EN_LOWER_LAST']:
            result += enToUga(char, isUpper=False)
        elif charNum >= STDCONST['EN_UPPER_FIRST'] and charNum <= STDCONST['EN_UPPER_LAST']:
            result += enToUga(char, isUpper=True)
        elif charNum >= STDCONST['NUM_FIRST'] and charNum <= STDCONST['NUM_LAST']:
            result += numToUga(char)
        result += ' '
    return result

def ugaToBin(char):
    char = char.replace('우', '0')
    char = char.replace('가', '1')
    return char

def ugaToNum(char):
    return chr(int(ugaToBin(char), 2) + STDCONST['NUM_FIRST'])

def ugaToEn(char):
    charBin = ugaToBin(char)
    charNum = int(charBin, 2)
    if charBin[0] == '0': # Lower
        charNum += STDCONST['EN_LOWER_FIRST']
    elif charBin[0] == '1': # Upper
        charNum += STDCONST['EN_UPPER_FIRST']
    return chr(charNum)

def ugaToKor(char):
    return chr(int(ugaToBin(char), 2) + STDCONST['KOR_FIRST'])

def ugaToText(text):
    result = ''
    for char in text.split():
        charLen = len(char)
        if charLen == 2:
            if char == '우가':
                result += ' '
        elif charLen == 4:
            result += ugaToNum(char)
        elif charLen == 6:
            result += ugaToEn(char)
        elif charLen == 16:
            result += ugaToKor(char)
    return result

def main():
    pass

if __name__ == '__main__':
    main()