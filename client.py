import socket

host, port = ('127.0.0.1', 6666)
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try :
    socket.connect((host, port))
    print("Client connecté")

    data = "Yop"
    data = data.encode("utf8")
    socket.sendall(data)

except:
    print('Connexion au serveur échouée')
finally:
    socket.close()
