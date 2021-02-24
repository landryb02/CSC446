# Made with Python 2.7.16
# Brandon Vessel
# CSC 442 / CYEN 301
# FTP (FTP.py)
# April 3, 2020
# updated for CSC 446 cyberstorm challenge

#import os
from ftplib import FTP
import sys

# sanity check
if(len(sys.argv) != 2):
    print("Usage python3 {} <folder name>".format(sys.argv[0]))

# bit length. 7 or 10
METHOD=7

# filepath
FOLDER=str(sys.argv[1])

# host information
HOST="brandtest.us.to"
PORT1=9611
PORT2=9612

# login information
USERNAME="anonymous"
PASSWORD=""


# fetch permissions from the current directory
def fetch_permissions(connection):
    # list of files
    files = []

    # append file list to files
    connection.dir(files.append)

    # return file list
    return files


# convert from seven bit permissions booleans to text
def seven_bit(ftp):
    # traverse to 7 bit directory
    ftp.cwd(FOLDER)

    # grab file permissions
    permissions = fetch_permissions(ftp)
    #for p in permissions:
        #print(p)

    # close connection
    ftp.quit()

    #print(permissions)

    bit_permissions = []
    # iterate through permissions
    for i in range(len(permissions)):
        # get file data from list
        file_data = permissions[i]

        # seperate the permissions from everything else
        file_data = file_data.split(" ")[0]

        # check first 3 bits
        first_three = "".join(list(file_data)[0:3])
        
        # only proceed if the first three bits are 0
        if(first_three == "---"):
            # chop off the bits we don't need
            file_data = "".join(list(file_data)[3:10])
            #print(file_data)

            # set the permissions value as the new string
            bit_permissions.append(file_data)
            #print(file_data)

    # return modified permission
    return bit_permissions


# convert from ten bit permissions booleans to text
def ten_bit(ftp):
    # traverse to 10 bit directory
    #ftp.cwd(FOLDER)

    # grab file permissions
    permissions = fetch_permissions(ftp)

    # close connection
    ftp.quit()

    # iterate through permissions
    for i in range(len(permissions)):
        # get file data from list
        file_data = permissions[i]

        # seperate the permissions from everything else
        file_data = file_data.split(" ")[0]

        # set the permissions value as the new string
        permissions[i] = file_data

    # return modified permissions
    return permissions


# the main decoding function for the first server
def decode1():
    # initiate connection
    # create FTP object
    ftp = FTP()

    # connect to server
    ftp.connect(HOST, PORT1)

    # login
    ftp.login(USERNAME, PASSWORD)


    # call specific bit function
    if(METHOD == 7):
        permissions = seven_bit(ftp)
    elif(METHOD == 10):
        permissions = ten_bit(ftp)

    # final binary string
    binary = []

    # convert from characters to binary
    for file_data in permissions:
        #print(file_data)
        file_data = str(file_data).replace("-","0").replace("w","1").replace("r","1").replace("x","1").replace("d", "1")
        #print(file_data)
        binary.append(file_data)
    
    # make binary into it's final form
    binary = "".join(binary)
    #print(binary)

    if(METHOD == 7):
        # only print 7 bit length
        return(binary_to_text(binary, 7))

    else:
        # since length is unknown, print 7 and 8 bit length ascii
        print("7 Bit:")
        return(binary_to_text(binary, 7))
        #print("8 Bit:")
        #print(binary_to_text(binary, 8))

# the main decoding function for the second server
def decode2():
    # initiate connection
    # create FTP object
    ftp = FTP()

    # connect to server
    ftp.connect(HOST, PORT2)

    # login
    ftp.login(USERNAME, PASSWORD)


    # call specific bit function
    if(METHOD == 7):
        permissions = seven_bit(ftp)
    elif(METHOD == 10):
        permissions = ten_bit(ftp)

    # final binary string
    binary = []

    # convert from characters to binary
    for file_data in permissions:
        #print(file_data)
        file_data = str(file_data).replace("-","0").replace("w","1").replace("r","1").replace("x","1").replace("d", "1")
        #print(file_data)
        binary.append(file_data)
    
    # make binary into it's final form
    binary = "".join(binary)
    #print(binary)

    if(METHOD == 7):
        # only print 7 bit length
        return(binary_to_text(binary, 7))

    else:
        # since length is unknown, print 7 and 8 bit length ascii
        print("7 Bit:")
        return(binary_to_text(binary, 7))
        #print("8 Bit:")
        #print(binary_to_text(binary, 8))

# converts binary to text give a string and bit length
# from Binary.py
def binary_to_text(data, step):

    fstring = []

    data = list(data)

    while(len(data) != 0):
        character = []
        # try catch in case of improper step
        try:
            for _ in range(step):
                # pop off only the characters we need
                character.append(data.pop(0))
        except:pass
        
        # make it a string
        character = "".join(character)

        # convert to ascii number base 10
        character = int(character, 2)
        #print("{} {}".format(character, chr(character)))

        # check for backspace
        if(int(character) == 8):
            # delete character before backspace
            _ = fstring.pop()

        # check for tab
        elif(int(character) == 9):
            # tab
            fstring.append("\t")
        # check for carraige return
        elif((int(character) == 10) or (int(character) == 13)):
            # new line
            fstring.append("\n")
        else:
            # add character to string list as an ascii character instead of its number
            fstring.append(chr(character))
        
    # return binary string
    return "".join(fstring)


# MAIN
if(__name__ == "__main__"):
    # previous text for server 1
    previous_text1 = ""
    # previous text for server 2
    previous_text2 = ""

    # current conversation index
    convo_index = 0

    # print server changes forever
    while(1):
        try:
            text1 = decode1()
            if text1 != previous_text1:
                previous_text1 = text1
                convo_index += 1
                print(convo_index, text1)
        except:pass
        try:
            text2 = decode2()
            if text2 != previous_text2:
                previous_text2 = text2
                convo_index += 1
                print(convo_index, text2)
        except:pass