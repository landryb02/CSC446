from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer
import os
import config

# make sub directories if they don't already exist
files = os.listdir(os.getcwd())
if "public1" not in files:
    try:os.mkdir("public1")
    except:
        print("[ERROR] Could not create 'public1' directory!")
        exit(1)
if "public2" not in files:
    try:os.mkdir("public2")
    except:
        print("[ERROR] Could not create 'public2' directory!")
        exit(1)

# get current directory and format
directory = os.getcwd()
directory1 = os.path.join(directory, "public1")
directory2 = os.path.join(directory, "public2")

# actually create ftp server
authorizer = DummyAuthorizer()

# create administrator
#authorizer.add_user(username=config.USERNAME, password=config.PASSWORD, homedir=directory1, perm="elradfmwMT")

# create anonymous user
authorizer.add_anonymous(homedir=directory1, perm="elr")

handler = FTPHandler
handler.authorizer = authorizer

server = FTPServer(('', int(config.PORT1)), handler)
server.serve_forever()