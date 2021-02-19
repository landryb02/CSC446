from ftplib import FTP
import config
import os
import random
from math import ceil
from time import time, sleep
import util


class Message():
    '''Represents a single entry of dialogue'''
    def __init__(self):
        # what server the message belongs to
        self.server = -1
        # the text of the message
        self.text = ""
        # the permission list of the message
        self.permissions = []


class Conversation():
    '''Represents a conversation'''
    def __init__(self, index):
        self.index = int(index)
        
        self.messages = []
        self.server1messages = 0
        self.server2messages = 0

        # current index in the conversation
        self.currentIndex = -1

        # length of the conversation
        self.convoLength = -1

        # load conversation
        self.loadConversation()

        # convert data into messages
        self.populateConversation()

        # generate permissions
        self.generatePermissions()

        # make sure folder exists on both servers
        # attempt to create
        try: os.mkdir(util.pathJoiner([os.getcwd(), "public1", index]))
        except:pass
        try: os.mkdir(util.pathJoiner([os.getcwd(), "public2", index]))
        except:pass

        #for i in self.messages:
            #print(i.text, i.server, i.permissions)
        
        # flush conversation directories (just in case)
        existing_files = os.listdir(util.pathJoiner([os.getcwd(), "public1", str(self.index)]))
        existing_files2 = os.listdir(util.pathJoiner([os.getcwd(), "public2", str(self.index)]))
        for i in existing_files:
            os.remove(util.pathJoiner([os.getcwd(), "public1", str(self.index), i]))
        for i in existing_files2:
            os.remove(util.pathJoiner([os.getcwd(), "public2", str(self.index), i]))


    def loadConversation(self):
        '''Loads the conversation into memory given the conversation number'''
        # variables for the file paths
        transcript_filename = util.pathJoiner([os.getcwd(), "conversations", str(self.index), "transcript.txt"])
        names_filename = util.pathJoiner([os.getcwd(), "conversations", str(self.index), "names.txt"])

        # lines in the transcript
        self.transcript = util.readFile(transcript_filename)

        # list of names in the conversation (corresponds to the server each is on)
        self.names = util.readFile(names_filename)

        # set length
        self.convoLength = len(self.transcript)
    

    def populateConversation(self):
        '''Formats the transcript into a discernable list of Messages'''
        # make a message for each chunk of text
        for text in self.transcript:
            # create Message instance
            mm = Message()

            # fill it with text
            mm.text = text
            
            # determine which server it belongs to based on who is talking
            if self.names[0] in text:
                mm.server = 1
            elif self.names[1] in text:
                mm.server = 2
            
            # put the message in the list
            self.messages.append(mm)


    def generatePermissions(self):
        '''Generates permissions for each message'''
        for q in range(len(self.messages) - 1):
            # split message into bits
            ms = list(self.messages[q].text)

            # make characters into list of binary characters
            k = []
            for i in range(len(ms)):
                #ms[i] = list(bin(ord(ms[i])))[2:]
                ms[i] = list('{:07b}'.format(ord(ms[i])))
                for j in ms[i]:
                    k.append(j)

            # get permissions ready (create sets of 7 bits)
            self.permissions = []

            while len(k) != 0:
                bits = []
                permission = []
                # get 7 bits
                for i in range(7):
                    try: bits.append(k.pop(0))
                    except: bits.append('0')

                # last bit of owner permissions
                permission.append(util.chmodMatch(['0', '0', bits[0]]))

                # group permissions
                permission.append(util.chmodMatch(bits[1:4]))

                # anyone permissions
                permission.append(util.chmodMatch(bits[4:7]))

                # put permission into message permissions list
                self.messages[q].permissions.append("".join(permission))


    def setMessage(self, message):
        '''Clears the conversation folder and set's a message'''
        start = time()
        
        files = getWords(len(message.permissions))
        files.sort()
        permissions = message.permissions
        folder = str(message.server)
        if(config.DEBUG):
            print(message.text)

        directory = util.pathJoiner([os.getcwd(), "public{}".format(folder), str(self.index)])

        # clear server (delete all files)
        existing_files = os.listdir(directory)
        for i in existing_files:
            os.remove(os.path.join(directory, i))

        # make files
        #makeFiles(pathJoiner([os.getcwd(), "public{}".format(), files, permissions)
        #makeFiles(os.path.join(os.getcwd(), "public1"), live_files, permissions)
        
        # generate each file and set permission
        for i in range(len(files)):
            filename = files[i]
            # file contents
            if(config.DEBUG):
                print(os.path.join(directory, filename))
            if filename.lower() == "snake":
                with open(os.path.join(directory, filename), "w") as f:
                    # write a little hint for those who look through the files
                    f.write("Excellent Snake. Age hasn't slowed you down one bit.\nHere's a hint: 7 bits, enough to kill anything that moves.")
            else:
                with open(os.path.join(directory, filename), "w") as f:
                    # literally means nothing
                    f.write("nope")
            
            # set permission
            #os.chmod(os.path.join(directory, filename), 0)
            #os.chmod(os.path.join(directory, filename), )
            os.system("chmod {} {}".format("".join(permissions[i]), os.path.join(directory, filename)))
            os.system("chmod u-w {}".format(os.path.join(directory, filename)))

        print("Time taken:", time() - start)
    
    
    def update(self):
        '''Advances the current message to the next piece of dialogue and updates the ftp server'''
        # move current index to the next place (within the list)
        self.currentIndex = (self.currentIndex + 1) % self.convoLength

        # update files
        #self.setMessage()
        self.setMessage(self.messages[self.currentIndex])

        # update console with message update
        print("Convo {} progress ({}/{}) server public{}".format(self.index, self.currentIndex, self.convoLength, self.messages[self.currentIndex].server))


def getWords(length):
    '''Get's a certain number of words from the wordlist'''
    global swordlist
    random.shuffle(swordlist)
    return swordlist[0:length]


def makeFiles(directory, files, permissions):
    '''Makes the files for the FTP server and sets their permissions'''
    for i in range(len(files)):
        filename = files[i]
        # file contents
        if filename.lower() == "snake":
            with open(os.path.join(directory, filename), "w") as f:
                f.write("Excellent Snake. Age hasn't slowed you down one bit.\nHere's a hint: 7 bits, enough to kill anything that moves.")
        else:
            with open(os.path.join(directory, filename), "w") as f:
                f.write("nope")
        
        # set permission
        #os.chmod(os.path.join(directory, filename), 0)
        #os.chmod(os.path.join(directory, filename), )
        os.system("chmod {} {}".format("".join(permissions[i]), os.path.join(directory, filename)))
        os.system("chmod u-w {}".format(os.path.join(directory, filename)))

        # debug
        #print("Making {}".format(filename))


def getConversations():
    '''Gets the conversations from the folder and returns a list of the classes'''
    conversations = []
    # iterate through each conversation folder (hence each conversation) using the numbers
    for convoID in os.listdir(os.path.join(os.getcwd(), "conversations")):
        # create a Conversation instance for each conversation and appends it to the list
        conversations.append(Conversation(convoID))

    # return list of conversations
    return conversations


# debug
print("Initializing")

# initialize chmod bit mapping dictionary
util.initializeBitstringMap()

# generate the wordlist so we don't have to read from the disk every time
# get words from 5 letter s words file
swordlist = util.readFile(os.path.join(os.getcwd(), os.path.join("dummydata", "swords.txt")))

#setMessage("".join(lines), ["public1", "1"])

# get conversations from conversations folder
conversations = getConversations()

# shuffle conversations so they update in a random order :)
# hehe
#random.shuffle(conversations)

print("Loaded. Beginning Main Loop")

# loop forever
while(1):
    # do a quick shuffle before each iteration just to mess with the challengers
    #random.shuffle(conversations) # DISABLED RN FOR TESTING PURPOSES
    # loop through each conversation and advance it
    for i in range(len(conversations)):
        conversations[i].update()
        # wait for a little bit
        sleep(config.SERVER_UPDATE_WAIT)