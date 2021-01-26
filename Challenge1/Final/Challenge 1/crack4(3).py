import hashlib
from binascii import hexlify
import sqlite3

pepper = hashlib.sha256()
pepper.update("I really love this stuff!".encode())
pepper = pepper.digest()



def importdb(db):
    conn = sqlite3.connect(db)
    c = conn.cursor()
    return c.execute("SELECT * FROM users")



def hexToBytes(hexdata):
    '''Convert hex string into bytes'''
    return bytes.fromhex(hexdata)



# get dictionary
with open("dictionary.txt") as f:
    dictionary_lines = f.readlines()

# convert dictionary into bytes
for i in range(len(dictionary_lines)):
    dictionary_lines[i] = bytes(dictionary_lines[i].rstrip(), "utf-8")


# get data
database_list = importdb("users.db")


# do each user
for entry in database_list:
    username = entry[0]
    password = hexToBytes(entry[1])
    salt = hexToBytes(entry[2])


    #print("\nbefore: "+username)
    #print(password)
    #print(salt)


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


    # password dictionary attack
    for i in range(len(dictionary_lines)):

        # iterate through every entry in the dictionary trying to crack the password hash
        # if salt+password hashed = hash, set actual password
        combined = salt + dictionary_lines[i] + hexlify(pepper)
        m = hashlib.sha256()
        m.update(combined)


        # if hashes match, the current password is correct
        if m.digest() == password:
            print(userDecoded + " => " + str(dictionary_lines[i].decode('utf-8')))
