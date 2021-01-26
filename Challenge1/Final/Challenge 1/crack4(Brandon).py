import hashlib
import sqlite3

pepper = hashlib.sha256()
pepper.update(b'I really love this stuff!')
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
    #dictionary_lines[i] = bytes(dictionary_lines[i].rstrip(), "utf-8")
    dictionary_lines[i] = dictionary_lines[i].rstrip().encode()
    
# get data
database_list = importdb("users.db")


testpass = "384108a218381973820b4123674ca2bf1aed89780750a0fcbf033c65b168f921"
testsalt = hexToBytes("1b2cffb05fd5823d6f73163af36e14ee")

for entry in dictionary_lines:
    if hashlib.sha256(testsalt + entry + pepper).hexdigest() == testpass:
        print("YAY")

#exit()

# do each user
for entry in database_list:
    username = entry[0]
    password = hexToBytes(entry[1])
    salt = hexToBytes(entry[2])

    #print(username)
    #print(entry[1])
    #print(salt)

    # password dictionary attack
    for i in range(len(dictionary_lines)):
        # iterate through every entry in the dictionary trying to crack the password hash
        # if salt+password+pepper hashed = hash, set actual password
        m = hashlib.sha256()
       
        m.update(salt)
        m.update(dictionary_lines[i])
        m.update(pepper)
        

        #print(hashlib.sha256(salt + dictionary_lines[i] + pepper).hexdigest())
        if m.digest() in password:
            print("FOUND => " + str(dictionary_lines[i]))

        #if hashlib.sha256(entry[2] + dictionary_lines[i]).hexdigest() == entry[1]

#hashlib.sha256(string.encode()).hexdigest()

print("DONE")