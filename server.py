import socket
import threading
from _thread import *
import time


count = 0;
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Socket successfully created")
except socket.error as err:
    print("socket creation failed with error %s" % err)

try:
    s.bind((socket.gethostname(), 500))

except socket.error as e:
    print(str(e))
s.listen(2)
print("socket is listening")


def connection(c, addr):
    global count
    print(f"Connected to {addr} ")
    while True:
        try:
            data = c.recv(2048)
            reply = data.decode('utf-8')
        except:
            break

        if reply == "CanIStart":
            count = count + 1

        while True:
            if count == 2:
                c.send(str.encode("Start"))
                break
            else:
                print("waiting for another client")
                time.sleep(1)




    # close connection
    # c.close();
    #print("[-] Client disconnected")


while True:
    c, addr = s.accept()
    # t = threading.Thread(target=connection, args=(c, addr))
    # t.start()
    start_new_thread(connection, (c, addr))
