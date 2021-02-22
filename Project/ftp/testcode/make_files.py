import os

def readFile(filename):
    '''Returns a list of the lines in a file'''
    with open(filename, "r") as f:
        k = f.readlines()
        for i in range(len(k)):
            k[i] = k[i].rstrip("\n")
        return k

swords = readFile(os.path.join(os.getcwd(), os.path.join("dummydata", "swords.txt")))

for i in swords:
    if i.lower() == "snake":
        with open(os.path.join(os.getcwd(), os.path.join("dummyfiles", i),), "w") as f:
            f.write("Excellent Snake. Age hasn't slowed you down one bit. You're pretty good.\nHere's a hint: 7 bullets, enough to kill anything that moves.")
    else:
        with open(os.path.join(os.getcwd(), os.path.join("dummyfiles", i),), "w") as f:
            f.write("nope")
    print("Making {}".format(i))