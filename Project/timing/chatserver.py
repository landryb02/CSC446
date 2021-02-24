import socket
from time import sleep
from binascii import hexlify

# enables debug printing
DEBUG = False

# set the port for client connections
port = 56540

# create the socket and bind it to the port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("", port))

delay_00 = 0.5
delay_01 = 1.0
delay_10 = 1.5
delay_11 = 2.0

# set the message
msg = "Signal Test: One, two, three, four. Anyone copy? Over."
covert_message="pliskin" + "EOF"

# turn covert message into bit message
covert_bin=[]

for i in covert_message:
    covert_bin += bin(int(hexlify(i.encode()), 16))[2:].zfill(8)

msg = list(msg)

# import thread module
from _thread import start_new_thread
import threading 

if(DEBUG):print(len(covert_bin))
if(DEBUG):print(covert_bin)

# thread function 
def serveClient(c):
    try:
        global covert_bin
        # send the message, one letter at a time
        # while there is still bit_message to send
        n=0
        done=False
        while(not done):
            for i in msg:
                # Get bits to send
                bit1 =  covert_bin[n]
                bit2 =  covert_bin[n+1]
                bits = [bit1, bit2]

                #if(DEBUG):print(bits)

                c.send(i.encode())
                if(bits == ['0','0']):
                    delay=delay_00
                elif(bits == ['0','1']):
                    delay=delay_01
                elif(bits == ['1','0']):
                    delay=delay_10
                else:
                    delay=delay_11
                    
                sleep(delay)
                if(DEBUG):print(delay)
                n = (n+2) % len(covert_bin)
                if(n==0):
                    done=True
                    break
                

        # send EOF and close the connection to the client
        c.send("EOF".encode())
        c.close()
    except:pass

print("Timing Server Initialized On Port: {}".format(port))

# a forever loop until client wants to exit 
while True:
    # listen for clients
    # this is a blocking call
    s.listen(0)

    # a client has connected!
    c, addr = s.accept()

    print("Incoming connection : {}:{}".format(addr[0], addr[1])) 

    # Start a new thread and return its identifier 
    start_new_thread(serveClient, (c,)) 
s.close() 
