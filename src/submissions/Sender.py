import socket
import logging
import random

logging.basicConfig(filename='test.log', level=logging.DEBUG, format='%(asctime)s')

rannum = random.randrange(0, 100)

logging.debug(rannum)

s = socket.socket()
host = socket.gethostname()
port = 8833
s.bind((host, port))
s.listen(1)
print(host)
print("Waiting for any incoming connections...")
conn, addr = s.accept()
print(addr, "Has connected to the server")

filename = input(str("Please enter the filename of the file:"))
file = open(filename, 'rb')
file_data = file.read(1024)
conn.send(file_data)
print("Data has been transmitted successfully")