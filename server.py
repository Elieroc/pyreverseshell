import socket

host, port = ('', 6666)

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.bind((host, port))
print('Le serveur est démarré !')

while True:
    socket.listen()
    conn, address = socket.accept()
    print("Un client vient de se connecter")

    data = conn.recv(1024)
    data = data.decode("utf8")
    print(data)

conn.close()
socket.close()
