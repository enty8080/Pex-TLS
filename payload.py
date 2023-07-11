import socket
import os

from pex.ssl import OpenSSL

ssl = OpenSSL()

s = socket.socket()
s.connect(('127.0.0.1', 8888))

cl = ssl.wrap_client(s, server=False)

while True:
	cl.send(cl.recv(1024))