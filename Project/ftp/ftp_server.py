from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

from os import getcwd

directory = getcwd()

authorizer = DummyAuthorizer()
authorizer.add_user("user", "12345", directory, perm="elradfmw")
authorizer.add_anonymous(directory, perm="elradfmw")

handler = FTPHandler
handler.authorizer = authorizer

server = FTPServer(("127.0.0.1", 8888), handler)
server.serve_forever()