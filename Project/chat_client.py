############################################################################################
#   Team: Phoenicians
#   GitHub: https://github.com/marcusjr98/CSC442/edit/master/chat_client.py
#   Discription: This code is made to recieve a covert message from a server that is 
#                transmitting a message with timed delays
############################################################################################

import socket
from time import time
from binascii import unhexlify
import sys

# set a DEBUG
DEBUG = 0

# DEBUG sets a list for delay times
if (DEBUG == 1):
    TimePrint = []

# Set the location we are pinging
IP = 'jeangourd.com'
PORT = 31337
# Set the delay that determines 0 r 1
DELAY = 0.05

# sets up the socket to recieve a message from the server
x = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
x.connect((IP, PORT))

# Start recieveing data
covBin = ""
data = x.recv(4096)

while(data.rstrip("\n") != "EOF"):
    sys.stdout.write(data)
    sys.stdout.flush()
    # Start timer
    d1 = time()
    # Recieve Data from server
    data = x.recv(4096)
    # Finish time
    d2 = time()
    # Find total time ellapsed to recieve a part of the message
    ellapsed = round(d2 - d1, 3)

    # Determine if that time ellapsed is a 0 or 1
    if(ellapsed >= DELAY):
        covBin += '1'
    if(ellapsed < DELAY):
        covBin += '0'

    # Add the ellapsed time to the DEBUG list
    if (DEBUG == 1):
        TimePrint.append(ellapsed)

# Print your DEBUG
if (DEBUG == 1):
    print TimePrint


covMssg = ""
i = 0
while (i < len(covBin)):
    # process one byte at a time
    b = covBin[i:i + 8]
    # convert it to ASCII
    n = int("0b{}".format(b), 2)
    try:
        covMssg += unhexlify("{0:x}".format(n))
    except TypeError:
        covMssg += "?"
    # stop at the string "EOF"
    i += 8

# Print final message
print ("Here Is Your Secret Message: '{}'".format(covMssg))
x.close()
