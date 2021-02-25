# try statement keeps the clients from seeing error statements
try:
    teamname = str(input("Team Name:")).rstrip()
    from colorama import Fore, Style
    from sys import stdout

    def greenify():
        '''Changes text color to green'''
        stdout.write(Fore.GREEN)

    greenify()
    uusername = str(input("Username:")).rstrip()

    import time
    from hashlib import sha256

    tfa = ""
    with open("username.txt") as f:
        tfa = f.readlines()[0]

    hashh = sha256(uusername.lower().encode() + b"salt me SALT ME").hexdigest()

    if hashh != tfa:
        print("Invalid username. This attempt has been logged.")
        time.sleep(1)
        exit()

    upas = str(input("Password:")).rstrip()
    tfa = ""
    with open("password.txt") as f:
        tfa = f.readlines()[0]

    hashh = sha256(upas.lower().encode() + b"salt me SALT ME").hexdigest()

    if hashh != tfa:
        print("Correct username. Incorrect password. This attempt has been logged. Your progress has been saved.")

        # log correct username
        import time
        ts = time.gmtime()
        # Iso Format
        ts = time.strftime("%c", ts)
        # Sun Feb 21 22:34:41 2021
        with open("log.txt", "a") as f:
            f.write("{} USERNAME CORRECT {}\n".format(ts, teamname))
        time.sleep(1)
        exit()
    else:
        print("Access Granted! Your progress has been saved.")
        
        # log correct password
        import time
        ts = time.gmtime()
        # Iso Format
        ts = time.strftime("%c", ts)
        with open("log.txt", "a") as f:
            f.write("{} PASSWORD CORRECT {}\n".format(ts, teamname))
        time.sleep(1)

    # access granted, import the other libraries
    import os
    from math import floor

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
        # get terminal dimensions
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

    def getWidth():
        '''Gets width of the terminal'''
        # get terminal dimensions
        return os.get_terminal_size()[0]

    def printRex():
        '''Prints metal gear rex ascii art'''
        os.system("./image2ascii -f Metal_Gear_Rex.png")

    def selfDestruct():
        '''Records the winning team name and destroys the system'''
        global teamname
        with open("guilty.txt", "a") as f:
            f.write(teamname)
            f.write("\n")
        os.system("tmux kill-session")

    def getTeamName():
        pass

    #def regionalInformation():
    #    print("")
    #    tmp=input()

    cls()

    # variables
    # whether or not to sleep
    PATSLEEP = True

    # sleep to fix display
    time.sleep(0.3)

    # print to fix display
    print(" ")

    # print robot
    printRex()

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
    printCenteredX("""[SYSTEM] REX Status: ONLINE                """)
    if PATSLEEP:time.sleep(3)
    printCenteredX("""[SYSTEM] LAUNCHING COMMAND INTERFACE       """)
    if PATSLEEP:time.sleep(3)

    resetColor()
    cls()

    from pick import pick
    class Node():
        def __init__(self, title):
            self.title = title
            self.children = {}
            self.options = []

        def run(self):
            '''Uses the title and options list to make user pick options for the menu'''
            # loop forever so when the child returns we come back here and pick again
            while(1):
                # make user pick from list
                result = pick(title=self.title, options=self.options)[0]

                # process exit case
                if result == "Disconnect":
                    exit()

                # process return case (and abort launch case)
                if result == "Return" or result == "ABORT":
                    return

                # process launch case (ending)
                if result == "LAUNCH":
                    # ending code here
                    print('''Congratulations! You have beaten the challenge!
Metal Gear REX has launched 8 ICBMs to all the network satellites.
It also has self-destructed and left a crater at the facility...
Your success has been recorded in the system logs.
The entire system will crash as soon as the missiles hit.
Do not be alarmed when everything crashes :).''')
                    from time import sleep
                    sleep(5)
                    selfDestruct()
                    
                # run child
                self.children[result].run()

    def createNodes():
        '''Creates all the nodes and returns the head'''
        # connection failed node
        conn_failed = Node("[ CONNECTION FAILED ]")
        conn_failed.options.append("Return")

        # access denied node
        denied = Node("[ ACCESS DENIED ]")
        denied.options.append("Return")

        # head node
        head = Node("Region selection")
        head.options = ["Africa [OFFLINE]"]

        # add head children
        head.children["Africa [OFFLINE]"] = conn_failed
        head.children["Asia East [OFFLINE]"] = conn_failed
        head.children["Asia SE-Mainland [OFFLINE]"] = conn_failed
        head.children["Asia SE-Maritime [OFFLINE]"] = conn_failed
        head.children["Canada [OFFLINE]"] = conn_failed
        head.children["Europe [OFFLINE]"] = conn_failed
        head.children["Middle East [OFFLINE]"] = conn_failed
        head.children["North Pole [OFFLINE]"] = conn_failed
        head.children["Oceana [OFFLINE]"] = conn_failed
        head.children["US-East [OFFLINE]"] = conn_failed
        head.children["US-West [OFFLINE]"] = conn_failed

        alaska = Node("Alaska [ONLINE]")
        alaska.options = ["Facilities", "Military Information", "Regional Information", "Return"]
        facilities = Node("Facilities")

        # facilities
        # add blank ones
        for base_name in ["Clear [OFFLINE]", "Eielson [ONLINE]", "Elmendorf [ONLINE]", "Fort Greely [OFFLINE]", "Fort Richardson [ONLINE]", "Fort Wainwright [ONLINE]", "ISC Kodiak [ONLINE]", "Juneau [ONLINE]"]:
            if "offline" in base_name.lower():
                facilities.children[base_name] = conn_failed
            else:
                facilities.children[base_name] = denied
            facilities.options.append(base_name)
        
        # add shadow moses
        shadow_moses = Node("Shadow Moses [ONLINE]")
        shadow_moses.options = ["Facility Management", "Military Information", "Nuclear Control System"]
        shadow_moses_military_information = Node('''Military Information
    Troop Information

    Artillery 28
    Bombers   13
    Fighters  26
    Infantry  10,842
    Tanks     34
    SPECIAL   8''')

        shadow_moses_military_information.options = ["Return"]

        shadow_moses.children["Military Information"] = shadow_moses_military_information

        # facility management
        facility_management = Node("Facility Management")
        facility_management.children["Power"] = denied
        facility_management.children["Water"] = denied

        facility_management.options = ["Power", "Water", "Return"]

        shadow_moses.children["Facility Management"] = facility_management

        # nuclear control system
        nuclear = Node("Nuclear Control System [CLASSIFIED]")
        nuclear.options.append("Metal Gear REX1 [ONLINE]")
        nuclear.options.append("Metal Gear REX2 [OFFLINE]")
        nuclear.options.append("Metal Gear REX3 [OFFLINE]")
        nuclear.options.append("Metal Gear REX4 [OFFLINE]")
        nuclear.options.append("Metal Gear REX5 [OFFLINE]")
        nuclear.options.append("Metal Gear REX6 [OFFLINE]")
        nuclear.options.append("Metal Gear REX7 [OFFLINE]")
        nuclear.options.append("Metal Gear REX8 [OFFLINE]")
        nuclear.options.append("Return")
        
        # rex1
        rex1 = Node('''Metal Gear REX1 [ONLINE]

    Status Disarmed

    Ammo
    • Bullets        300,000
    • Nuclear ICBMs  8
    • Rockets        16,000''')

        rex1.options = ["Nuclear Launch Option", "Return"]

        # nuclear launch
        nuclear_launch = Node('''Metal Gear REX1 Nuclear Launch System

    WARNING!!! WARNING!!! WARNING!!!

    Metal Gear REX1 is currently set to mode: Physical Network Deletion Failsafe
    REX1 is set to target:
    • Satellite AL
    • Satellite GW
    • Satellite JD
    • Satellite TJ
    • Satellite TR
    • Shadow Moses
    Description: REX1 is currently programmed to eliminate the entire PMGGCS and itself
    in the event of enemy capture or automated defense system malfunction.

    Confirm launch?''')
        nuclear_launch.options = ["LAUNCH", "ABORT"]
        rex1.children["Nuclear Launch Option"] = nuclear_launch

        nuclear.children["Metal Gear REX1 [ONLINE]"] = rex1
        nuclear.children["Metal Gear REX2 [OFFLINE]"] = conn_failed
        nuclear.children["Metal Gear REX3 [OFFLINE]"] = conn_failed
        nuclear.children["Metal Gear REX4 [OFFLINE]"] = conn_failed
        nuclear.children["Metal Gear REX5 [OFFLINE]"] = conn_failed
        nuclear.children["Metal Gear REX6 [OFFLINE]"] = conn_failed
        nuclear.children["Metal Gear REX7 [OFFLINE]"] = conn_failed
        nuclear.children["Metal Gear REX8 [OFFLINE]"] = conn_failed

        # add nuclear to shadow moses
        shadow_moses.children["Nuclear Control System"] = nuclear

        # add shadow moses to alaska
        facilities.children["Shadow Moses Island [ONLINE]"] = shadow_moses
        facilities.options.append("Shadow Moses Island [ONLINE]")

        alaska_military_information = Node('''Military Information
    Troop Information

    Artillery 247
    Bombers   20
    Fighters  68
    Infantry  54,763
    Tanks     70
    SPECIAL   8

    Bases     10''')

        regional_information = Node('''Regional Information

    Latitude  51°20'N to 71°50'N
    Longitude 130°W to 172°E

    Government
    • Country       United States
    • Capital       Juneau
    • Largest city  Anchorage
    • Largest metro Anchorage metropolitan area

    Area
    • Total   663,268 sq mi (1,717,856 km²)
    • Land    571,951 sq mi (1,481,346 km²)
    • Water   91,316 sq mi (236,507 km²)  13.77%

    Dimensions
    • Length  1,420 mi (2,285 km)
    • Width   2,261 mi (3,639 km)

    Population
    • Total   710,249
    • Density 1.26/sq mi (0.49/km²)''')

        # add last empty base to facilities
        facilities.children["Valdez [OFFLINE]"] = conn_failed
        facilities.options.append("Valdez [OFFLINE]")

        facilities.options.append("Return")
        alaska_military_information.options.append("Return")
        regional_information.options.append("Return")

        alaska.children["Facilities"] = facilities
        alaska.children["Military Information"] = alaska_military_information
        alaska.children["Regional Information"] = regional_information

        facilities = Node("Facilities")

        # add alaska
        head.children["Alaska [ONLINE]"] = alaska
        head.options.append("Alaska [ONLINE]")

        # add other territories
        for territory in ["Asia East [OFFLINE]", "Asia SE-Mainland [OFFLINE]", "Asia SE-Maritime [OFFLINE]", "Canada [OFFLINE]", "Europe [OFFLINE]", "Middle East [OFFLINE]", "North Pole [OFFLINE]", "Oceana [OFFLINE]", "US-East [OFFLINE]", "US-West [OFFLINE]"]:
            head.children[territory] = conn_failed
            head.options.append(territory)

        head.options.append("Disconnect")

        return head

    # create and run the control menu
    head = createNodes()
    head.run()
except:pass