# maps 3 bit strings to a number for chmod
bitstringDict = {}

def readFile(filename):
    '''Returns a list of the lines in a file'''
    with open(filename, "r") as f:
        k = f.readlines()
        for i in range(len(k)):
            k[i] = k[i].rstrip("\n")
        return k


def readFileRaw(filename):
    '''Reads a file, but doesn't strip the lines'''
    with open(filename, "r") as f:
        k = f.readlines()
        return "".join(k)


def pathJoiner(directories):
    '''Makes the correct path string given a list of directories (and maybe a file)'''
    # make sure actually given something
    if len(directories) == 0:
        return ""
    
    # import join for concatenating path names
    from os.path import join
    # pop first index
    output = directories.pop(0)

    # add all other indexes properly
    for level in directories:
        output = join(output, level)

    # return string
    return output


def initializeBitstringMap():
    '''Initializes the bitstring dictionary'''
    global bitstringDict
    bitstringDict["000"] = '0'
    bitstringDict["001"] = '1'
    bitstringDict["010"] = '2'
    bitstringDict["011"] = '3'
    bitstringDict["100"] = '4'
    bitstringDict["101"] = '5'
    bitstringDict["110"] = '6'
    bitstringDict["111"] = '7'


def chmodMatch(bits):
    '''Matches 3 bits to a number. Yes it's actually that simple'''
    bits="".join(bits)
    if   bits == "000": return '0'
    elif bits == "001": return '1'
    elif bits == "010": return '2'
    elif bits == "011": return '3'
    elif bits == "100": return '4'
    elif bits == "101": return '5'
    elif bits == "110": return '6'
    elif bits == "111": return '7'
    else:
        print("[ERROR] Incorrect bit pattern in chmodMatch")
        exit(1)