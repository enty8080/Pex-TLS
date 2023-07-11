from hatsploit.lib.handler.misc import HatSploitSession

from pex.ssl import OpenSSL

import socket

ssl = OpenSSL()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
s.bind(('127.0.0.1', 8888))
s.listen()
c, a = s.accept()

cl = ssl.wrap_client(c)

session = HatSploitSession()
session.open(cl)

session.interact()