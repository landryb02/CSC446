###################################
# Name: Big Covert
# Class: CSC 446
# Challenge 1: DB 4
# Date: 1/12/2021
###################################
import hashlib
import sqlite3
from binascii import hexlify

########################
#        CONFIG        #
# pepper for salt + password + hash(pepper)
pepper_string = b"I really love this stuff!"

# enable debug mode
DEBUG = False
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

# compute pepper
pepper = hashlib.sha256()
pepper.update(pepper_string)
pepperhash = pepper.digest()

if(DEBUG):
    print("Pepper: ", pepper.hexdigest())

# do each user
for entry in database_list:
    username = entry[0].rstrip()
    password = hexToBytes(entry[1])
    salt = hexToBytes(entry[2])

    # debug print out each entry's information
    if(DEBUG):
        print("Username     :", username)
        print("Deciphered   :", deROT(username))
        print("Password hash:", entry[1])
        print("Salt         :", salt)

    # password dictionary attack
    for i in range(len(dictionary_lines)):
        # iterate through every entry in the dictionary trying to crack the password hash
        # if salt + password + hash(pepper) hashed = hash, set actual password
        m = hashlib.sha256(salt + dictionary_lines[i] + hexlify(pepperhash))
        
        # check to see if byte output of hash equals byte representation of hashed password
        if m.digest() == password:
            print(deROT(username) + " > " + dictionary_lines[i].decode())
            break