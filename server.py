#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import SocketServer
import os
import sys

class EchoHandler(SocketServer.DatagramRequestHandler):
    """
    Echo server class
    """

    def handle(self):
        # Escribe dirección y puerto del cliente (de tupla client_address)
        self.wfile.write("Hemos recibido tu peticion" + "\r\n")
        while 1:

            # Leyendo línea a línea lo que nos envía el cliente
            
            line = self.rfile.read()
            entrada = line.split(" ")
            IP = self.client_address

            print "El cliente nos manda " + line

            metodo = entrada[0]
            division = entrada[1].split("@")
            IP = division[1]

            #Metodos servidor INVITE , BYE
            
            if metodo == 'INVITE':
                print("Recibe invite")
                self.wfile.write("SIP/2.0 100 Trying" + "\r\n")
                self.wfile.write("SIP/2.0 180 Ring" + "\r\n")
                self.wfile.write("SIP/2.0 200 OK" + "\r\n")

            elif metodo == 'ACK':
                print "ACK recibido"
                Shell = "./mp32rtp -i " + IP + " -p " + "23032" + \
                            " < " + fich_audio
                print "Enviando RTP..."
                os.system(Shell)

            elif metodo == 'BYE':
                print "BYE recibido"
                self.wfile.write("SIP/2.0 200 OK")

            # Si no hay más líneas salimos del bucle infinito
            if not line:
                break

if __name__ == "__main__":
    # Creamos servidor de eco y escuchamos
    entrada = sys.argv
    #controlamos la entrada de argumentos
    if len(entrada) != 4:
        print "Numero incorrecto de argumentos."
        sys.exit()

    SERVER = entrada[1]
    PORT = entrada[2]
    fich_audio = sys.argv[3]
    serv = SocketServer.UDPServer(("", int(sys.argv[2])), EchoHandler)
    print "Listening..."
    try:
        serv.serve_forever()
    except:
        print "Usage: python servidor.py IP port audio_file"
        sys.exit()
