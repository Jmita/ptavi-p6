#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import socket
import sys

# Datos introducidos
metodo = sys.argv[1]
print metodo
division = sys.argv[2].split("@")
nick = division[0]
division2 = division[1].split(":")
IP = division2[0]
PORT = int(division2[1])

# Creamos el socket, lo configuramos y lo atamos a un servidor/puerto
my_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
my_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
my_socket.connect((IP, PORT))

if metodo == 'INVITE':
    line = "INVITE sip:" + nick + "@" + IP + " SIP/2.0"
elif metodo == 'BYE':
    line = "BYE sip:" + nick + "@" + IP + " SIP/2.0"
else:
    print "Usage: python cliente.py method receiver@IP:SIPport"
    sys.exit()

print "Enviando: " + line
my_socket.send(line + '\r\n')

try:
    data = my_socket.recv(1024)
    info = data.split("\r\n")
    print "Recibido -- " + data

except:
    print "Fallo de recepcion"

my_socket.close()
print "Terminando socket..."
