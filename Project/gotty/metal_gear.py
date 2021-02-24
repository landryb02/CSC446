from colorama import Fore, Style
from sys import stdout

def greenify():
    '''Changes text color to green'''
    stdout.write(Fore.GREEN)

greenify()
uusername = str(input("Username:")).rstrip()
upas = str(input("Password:")).rstrip()

import time
from hashlib import sha256

tfa = ""
with open("password.txt") as f:
    tfa = f.readlines()[0]

hashh = sha256(upas.lower().encode() + b"salt me SALT ME").hexdigest()

if hashh != tfa:
    print("Incorrect. This attempt has been logged.")
    time.sleep(1)
    exit()
else:
    print("Access Granted!")
    time.sleep(1)

from os import get_terminal_size

ascii_rex = ""
with open("rex.txt") as f:
    ascii_rex = "".join(f.readlines())

def printCenteredX(text):
    '''Prints text centered in the terminal on the X axis'''
    # get terminal width
    width = get_terminal_size()[0]

    # break string into lines
    lines = text.split("\n")

    # print each line
    for line in lines:
        # get length of line
        length = len(line)

        # figure out padding
        padding = int((width-length)/2)

        # print with padding
        print(" "*padding, line)

def resetColor():
    '''Resets the color of the terminal'''
    stdout.write(Style.RESET_ALL)

def cls():
    '''Clears the screen'''
    stdout.write(chr(27)+'[2j' + '\033c' + '\x1b')

def printCentered(text):
    '''Prints text centered square in the terminal'''
    # get terminal dimentions
    dimensions = get_terminal_size()

    # get height
    height = dimensions[1]

    # get width
    width = dimensions[0]

    # break string into lines
    lines = text.split("\n")

    # figure out where we need to start printing
    startHeight = int((height - len(lines))/2)

    # print until we get where we need to be
    for _ in range(startHeight):
        print("")

    # print each line
    for line in lines:
        # get length of line
        length = len(line)

        # figure out padding
        padding = int((width-length)/2)

        # print with padding
        print(" "*padding, line)


#@print("{}".format(ascii_rex))
cls()
greenify()
printCentered("{}".format(ascii_rex))

PATSLEEP = True

#printCenteredX("\nWelcome to the Patriot Global MG Control System")
#if PATSLEEP:time.sleep(2)
#printCenteredX("""---- PGMGCS v1.2 ----""")
#if PATSLEEP:time.sleep(3)
#printCenteredX("""[SYSTEM] CONFIGURING ENCRYPTED CHANNEL """)
#if PATSLEEP:time.sleep(3)
#printCenteredX("""[SYSTEM] CONNECTION ESTABLISHED        """)
#if PATSLEEP:time.sleep(1.5)
#printCenteredX("""[SYSTEM] CONNECTING TO REX 1           """)
#if PATSLEEP:time.sleep(3)
#printCenteredX("""[SYSTEM] Rex Unit 1 Status: ONLINE     """)
#if PATSLEEP:time.sleep(3)
#printCenteredX("""[SYSTEM] LAUNCHING COMMAND INTERFACE   """)
#if PATSLEEP:time.sleep(3)

#cls()
resetColor()
cls()
import os

os.system("bash")











def completed():
  global selfdestructable
  teamname = str(input("Congrats. You finished. Input your team name:"))
  
  with open("output.txt", "w") as f:
      f.write("{} {}\n".format(teamname, time.time()))
  print("You can keep playing with the system if you want...")
  selfdestructable = True

selfdestruct = str(input("Would you like to self-destruct?"))
os.system("./image2ascii -f Metal_Gear_Rex.png")
time.sleep(99)

'''
import curses

# The `screen` is a window that acts as the master window
# that takes up the whole screen. Other windows created
# later will get painted on to the `screen` window.
screen = curses.initscr()

# lines, columns, start line, start column
my_window = curses.newwin(15, 20, 0, 0)

# Long strings will wrap to the next line automatically
# to stay within the window
my_window.addstr(4, 4, "Hello from 4,4")
my_window.addstr(5, 15, "Hello from 5,15 with a long string")

# Print the window to the screen
my_window.refresh()
curses.napms(2000)

# Clear the screen, clearing my_window contents that were printed to screen
# my_window will retain its contents until my_window.clear() is called.
screen.clear()
screen.refresh()

# Move the window and put it back on screen
# If we didn't clear the screen before doing this,
# the original window contents would remain on the screen
# and we would see the window text twice.
my_window.mvwin(10, 10)
my_window.refresh()
curses.napms(1000)

# Clear the window and redraw over the current window space
# This does not require clearing the whole screen, because the window
# has not moved position.
my_window.clear()
my_window.refresh()
curses.napms(1000)

curses.endwin()
'''