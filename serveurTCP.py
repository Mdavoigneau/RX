#!/usr/local/bin/python3
# (Sur mon PC python est localisé dans /usr/local/bin)
import socket
import sys

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except Exception as e:
    print("Error while creating server socket !")
    sys.exit(1)

s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
s.bind(("", 7777)) # Greffe de s au port 7777 et écoute sur toutes les cartes
s.listen(1)        # On accepte les connexions sur s

while True:
    new_s = s.accept()
    client = new_s[0]
    while True:
        data = client.recv(1500)
        if len(data) == 0:
            break
        client.sendall(data)
    s.close()
