#!/usr/local/bin/python3
# (Sur mon PC python est localisé dans /usr/local/bin)
import socket
import sys

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except Exception as e:
    print("Socket error !")
    sys.exit(1)

host = sys.argv[1]
port = 80
request = "GET / HTTP/1.1\r\n"  \
    "Host: " + host + "\r\n"    \
    "Connection: close\r\n\r\n"

try:
    s.connect((host, port))
except Exception as e:
    print("Connection error ! Did you attempt to connect to localhost ?")
    sys.exit(1)

try:
    s.sendall(request.encode("utf-8"))
except Exception as e:
    print("Error while sending request !")
    sys.exit(1)

try:
    data = s.recv(15) # Taille 15 = Affichage des 15 premiers caractères.
except Exception as e:
    print("Error while receiving data !")
    sys.exit(1)

if data.decode("utf-8") == "HTTP/1.1 200 OK":
    while data != b"":
        # Decode permet de transformer des octets en string formaté en utf-8.
        print(data.decode("utf-8"), end="")
        data = s.recv(1024)
else:
    print("The request is not correct. Please check it.")
    s.close()
