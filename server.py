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
        while 1:
            # Leyendo línea a línea lo que nos envía el cliente
            line = self.rfile.read()
            entrada = line.split(" ")
            IP = self.client_address
            metodo = entrada[0]
            # Si no hay más líneas salimos del bucle infinito
            if not line:
                break
            #Metodos servidor INVITE , BYE
            print line
            if metodo == 'INVITE':
                self.wfile.write("SIP/2.0 100 Trying\r\n")
                self.wfile.write("SIP/2.0 180 Ringing\r\n")
                self.wfile.write("SIP/2.0 200 OK\r\n")
            elif metodo == 'ACK':
                Shell = ("./mp32rtp -i " + IPS + " -p " + "23032" +
                         " < " + fich_audio)
                print "Enviando RTP..."
                os.system(Shell)
                print "Terminado RTP"
                self.wfile.write("SIP/2.0 200 OK")
            elif metodo == 'BYE':
                self.wfile.write("SIP/2.0 200 OK")
            else:
                print "SIP/2.0 400 Bad Request"

if __name__ == "__main__":
    # Creamos servidor de eco y escuchamos
    entrada = sys.argv
    #controlamos la entrada de argumentos
    if len(entrada) != 4:
        print "Usage: python servidor.py IP port audio_file"
        sys.exit()
    IPS = entrada[1]
    PORT = entrada[2]
    fich_audio = sys.argv[3]
    serv = SocketServer.UDPServer(("", int(sys.argv[2])), EchoHandler)
    #print(sys.argv[2])
    print "Listening..."
    serv.serve_forever()
