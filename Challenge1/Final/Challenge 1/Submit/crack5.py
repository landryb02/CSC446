###################################
# Name: Big Covert
# Class: CSC 446
# Challenge 1: DB 5
# Date: 1/12/2021
###################################
import bcrypt
import hashlib
import sqlite3

########################
#        CONFIG        #
# enable debug mode
DEBUG = True
########################


def importdb(db):
    '''Imports the database'''
    conn = sqlite3.connect(db)
    c = conn.cursor()
    return c.execute("SELECT * FROM users")


def hexToBytes(hexdata):
    '''Convert hex string into bytes'''
    return bytes.fromhex(hexdata)


def deROT(username):
    '''De-ROT's the information'''
    # decode usernames by applying a ROT-1
    userDecoded = ""
    alphabet="zabcdefghijklmnopqrstuvwxyz"
    for char in username:

        # lowercase letter
        if char in alphabet:
            i = alphabet.index(char,1)
            userDecoded += alphabet[i-1]

        # uppercase letter
        elif char in alphabet.upper():
            i = alphabet.upper().index(char,1)
            userDecoded += alphabet.upper()[i-1]

        # not a letter
        else:
            userDecoded += char

    return userDecoded


# read dictionary into memory
with open("dictionary.txt") as f:
    dictionary_lines = f.readlines()

# rstrip dictionary and convert into bytes
for i in range(len(dictionary_lines)):
    dictionary_lines[i] = dictionary_lines[i].rstrip().encode()

# read database
database_list = importdb("users.db")


for entry in database_list:
    username = entry[0]
    password = entry[1].encode()

    for i in range(len(dictionary_lines)):
        if bcrypt.checkpw(dictionary_lines[i], password):
            print(deROT(username) + " > " + dictionary_lines[i].decode())
            break
    else:
        print("Unable to crack {}:{}!".format(deROT(username), password))