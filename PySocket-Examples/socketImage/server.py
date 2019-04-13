import socket
import threading
import os

def RetrFile(name, s):
    data = s.recv(1024)
    f = open('newfile.jpg', 'wb')
    f.write(data)
    while data != bytes(''.encode()):
        #print(data)
        data = s.recv(1024)
        f.write(data)

    s.close()

def Main():
    host = '127.0.0.1'
    port = 4999


    s = socket.socket()
    s.bind((host,port))

    s.listen(5)

    print ("Server Started.")
    while True:
        c, addr = s.accept()
        print ("client connedted ip:<" + str(addr) + ">")
        t = threading.Thread(target=RetrFile, args=("RetrThread", c))
        t.start()
         
    s.close()

if __name__ == '__main__':
    Main()