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

#if hashh != tfa:
#    print("Invalid username. This attempt has been logged.")
#    time.sleep(1)
#    exit()

tfa = ""
with open("password.txt") as f:
    tfa = f.readlines()[0]

hashh = sha256(upas.lower().encode() + b"salt me SALT ME").hexdigest()

#if hashh != tfa:
#    print("Incorrect password. This attempt has been logged.")
#    time.sleep(1)
#    exit()
#else:
#    print("Access Granted!")
#    time.sleep(1)

# access granted, import the other libraries
import os

def printCenteredX(text):
    '''Prints text centered in the terminal on the X axis'''
    # get terminal width
    width = os.get_terminal_size()[0]

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
    dimensions = os.get_terminal_size()

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

def printRex():
    '''Prints metal gear rex ascii art'''
    os.system("./image2ascii -f Metal_Gear_Rex.png")

# menu functions
def completeMission():
    global selfdestructable
    teamname = str(input("Congrats. You finished. Input your team name:"))
    
    with open("output.txt", "w") as f:
        f.write("{} {}\n".format(teamname, time.time()))
    print("You can keep playing with the system if you want...")
    selfdestructable = True

def selfDestruct():
    global selfdestructable
    global teamname
    if (selfdestructable):
        print("YAY")
        time.sleep(0.3)

def getTeamName():
    pass

#def regionalInformation():
#    print("")
#    tmp=input()

cls()

# variables
# whether or not to sleep
PATSLEEP = False

# sleep to fix display
time.sleep(0.3)

# print to fix display
print(" ")

time.sleep(1)
printCenteredX("\nWelcome to the Patriot Metal Gear Global Control System")
if PATSLEEP:time.sleep(1)
printCenteredX("""---- PMGGCS v1.2 ----""")
if PATSLEEP:time.sleep(3)
printCenteredX("""[SYSTEM] CONFIGURING TLS ENCRYPTED CHANNEL """)
if PATSLEEP:time.sleep(3)
printCenteredX("""[SYSTEM] CONNECTION ESTABLISHED            """)
if PATSLEEP:time.sleep(1.5)
printCenteredX("""[SYSTEM] CHECKING USER AUTHORIZATION       """)
if PATSLEEP:time.sleep(1.5)
printCenteredX("""[SYSTEM] TOP SECRET CLEARANCE GRANTED      """)
if PATSLEEP:time.sleep(1.5)
printCenteredX("""[SYSTEM] CONNECTING TO REX 1               """)
if PATSLEEP:time.sleep(3)
printCenteredX("""[SYSTEM] Rex Unit 1 Status: ONLINE         """)
if PATSLEEP:time.sleep(3)
printCenteredX("""[SYSTEM] LAUNCHING COMMAND INTERFACE       """)
if PATSLEEP:time.sleep(3)

resetColor()
cls()

#selfdestruct = str(input("Would you like to self-destruct?"))
#if "y" in selfdestruct.lower():
#    os.system("tmux kill-session ")



# Import the necessary packages
from cursesmenu import *
from cursesmenu.items import *

## Create the menu
#menu = CursesMenu(title="---- PMGGCS v1.2 ----", subtitle="Select Region")#, show_exit_option=True)
#
#oceania_getteamname = FunctionItem("Reset Database", getTeamName) # gets the team name
#
## oceana submenu
## final menu
#mg_menu = FunctionItem("Self Destruct [WARNING: IRREVERSIBLE. MAY CAUSE SYSTEM FAILURE", selfDestruct)
#
## troop movement menu
#troop_menu = CursesMenu("Penis", "subtitle")
#troop_menu.append_item(MenuItem("Fuck\nFuckfuck"))
#
#oceania_menu2 = CursesMenu()
#oceania_menu2.append_item(SubmenuItem("Oceania [ONLINE]", mg_menu)) # oceana submenu
#oceania_menu2.append_item(FunctionItem("Regional Information", selfDestruct)) # prints regional information
#oceania_menu2.append_item(FunctionItem("Troop Movement", troop_menu)) # prints troop movements
#oceania_menu2.append_item(FunctionItem("Metal Gear Nuclear Control System", mg_menu))
#oceania_main = SubmenuItem("Oceania [ONLINE]", oceania_menu2) # oceania selection from main
#
## append all items
#menu.append_item(MenuItem("Africa [OFFLINE]"))
#menu.append_item(MenuItem("Asia East [OFFLINE]"))
#menu.append_item(MenuItem("Asia SE-Mainland [OFFLINE]"))
#menu.append_item(MenuItem("Asia SE-Maritime [OFFLINE]"))
#menu.append_item(MenuItem("Canada [OFFLINE]"))
#menu.append_item(MenuItem("Europe [OFFLINE]"))
#menu.append_item(MenuItem("Middle East [OFFLINE]"))
#menu.append_item(MenuItem("North Pole [OFFLINE]"))
#menu.append_item(oceania_main)
#menu.append_item(MenuItem("US-East [OFFLINE]"))
#menu.append_item(MenuItem("US-West [OFFLINE]"))
#menu.append_item(ExitItem("Exit"))
#
## A FunctionItem runs a Python function when selected
#function_item = FunctionItem("Call a Python function", completeMission)
#
## A CommandItem runs a console command
#command_item = CommandItem("Run a console command",  "touch hello.txt")
#
## A SelectionMenu constructs a menu from a list of strings
#selection_menu = SelectionMenu(["item1", "item2", "item3"])
#
## A SubmenuItem lets you add a menu (the selection_menu above, for example)
## as a submenu of another menu
#
#
## Once we're done creating them, we just add the items to the menu
##menu.append_item(menu_item)
##menu.append_item(function_item)
##menu.append_item(command_item)
##menu.append_item(submenu_item)
##menu.append_item(menu_item)
##menu.append_item()

# Create the menu
menu = CursesMenu("Title", "Subtitle")

# Create some items

# MenuItem is the base class for all items, it doesn't do anything when selected
menu_item = MenuItem("Menu Item")

# A FunctionItem runs a Python function when selected
function_item = FunctionItem("Call a Python function", input, ["Enter an input"])

# A CommandItem runs a console command
command_item = CommandItem("Run a console command",  "touch hello.txt")

# A SelectionMenu constructs a menu from a list of strings
selection_menu = SelectionMenu(["item1", "item2", "item3"])

# A SubmenuItem lets you add a menu (the selection_menu above, for example)
# as a submenu of another menu
submenu_item = SubmenuItem("Submenu item", selection_menu, menu)

# Once we're done creating them, we just add the items to the menu
menu.append_item(menu_item)
menu.append_item(function_item)
menu.append_item(command_item)
menu.append_item(submenu_item)

# Finally, we call show to show the menu and allow the user to interact
menu.show()