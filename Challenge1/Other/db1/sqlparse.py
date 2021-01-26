import hashlib
import sqlite3

def importdb(db):
    conn = sqlite3.connect(db)
    c = conn.cursor()
    return c.execute("SELECT * FROM users")

string = "saltedpassword"

for thing in importdb("users.db"):
    print(thing[0])

# get dictionary
with open("dictionary.txt") as f:
    lines = f.readlines()
#this parses dictionary words
for i in range(len(lines)):
    lines[i] = lines[i].rstrip()





hashlib.sha256(string.encode()).hexdigest()

#database_list = importdb("users.db")
