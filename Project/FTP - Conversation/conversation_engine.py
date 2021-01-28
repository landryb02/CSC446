from ftplib import FTP
import config
import os
import random
from math import ceil
from time import time, sleep


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


def getWords(length):
    '''Get's a certain number of words from the wordlist'''
    global swordlist
    random.shuffle(swordlist)
    return swordlist[0:length]


def ftpLogin1():
    '''Connects to the first server'''
    # initiate connection
    # create FTP object
    ftp = FTP()

    # connect to server
    ftp.connect(config.SERVER1, int(config.PORT1))

    # login
    ftp.login(config.USERNAME, config.PASSWORD)

    return ftp


def ftpLogin2():
    '''Connects to the second server'''
    ftp = FTP(host=config.SERVER2, user=config.USERNAME, passwd=config.PASSWORD)
    ftp.connect(config.SERVER2,int(config.PORT2))
    ftp.login()
    return ftp


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


def makeFiles(directory, files, permissions):
    '''Makes the files for the FTP server and sets their permissions'''
    for i in range(len(files)):
        filename = files[i]
        # file contents
        #if filename.lower() == "snake":
        with open(os.path.join(directory, filename), "w") as f:
            f.write("Excellent Snake. Age hasn't slowed you down one bit. You're pretty good.\nHere's a hint: 7 bullets, enough to kill anything that moves.")
        #else:
        #    with open(os.path.join(directory, filename), "w") as f:
        #        f.write("nope")
        
        # set permission
        #os.chmod(os.path.join(directory, filename), 0)
        #os.chmod(os.path.join(directory, filename), )
        os.system("chmod {} {}".format("".join(permissions[i]), os.path.join(directory, filename)))
        os.system("chmod u-w {}".format(os.path.join(directory, filename)))

        # debug
        #print("Making {}".format(filename))


def setMessage1(message):
    '''Clears the server and set's a message'''
    start = time()
    # split message into bits
    ms = list(message)

    # make characters into list of binary characters
    k = []
    for i in range(len(ms)):
        #ms[i] = list(bin(ord(ms[i])))[2:]
        ms[i] = list('{:07b}'.format(ord(ms[i])))
        for j in ms[i]:
            k.append(j)

    # get new filenames
    live_files = getWords(ceil(float(len(k))/7.0))
    live_files.sort()
    print("Bits:", len(k))
    print("Length:", ceil(float(len(k))/7.0))

    # get permissions ready (create sets of 7 bits)
    permissions = []

    while len(k) != 0:
        bits = []
        permission = []
        # get 7 bits
        for i in range(7):
            try: bits.append(k.pop(0))
            except: bits.append('0')

        # last bit of owner permissions
        permission.append(chmodMatch(['0', '0', bits[0]]))

        # group permissions
        permission.append(chmodMatch(bits[1:4]))

        # anyone permissions
        permission.append(chmodMatch(bits[4:7]))

        permissions.append("".join(permission))

    # clear server (delete all files)
    files = os.listdir(os.path.join(os.getcwd(), "public1"))
    for i in files:
        os.remove(os.path.join(os.getcwd(), os.path.join("public1", i)))

    # make files
    makeFiles(os.path.join(os.getcwd(), "public1"), live_files, permissions)

    print("Time taken:", time() - start)

# generate the wordlist so we don't have to read from the disk every time
# get words from 5 letter s words file
swordlist = readFile(os.path.join(os.getcwd(), os.path.join("dummydata", "swords.txt")))

# get conversation
lines = readFileRaw("test.txt")

# conversation loop
#setMessage1("abcd")
setMessage1("".join(lines))