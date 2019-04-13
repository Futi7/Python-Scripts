import socket
import pygame
import pygame.camera

def Main():

    pygame.camera.init()
    cam = pygame.camera.Camera("/dev/video0",(640,480))
    cam.start()
    img = cam.get_image()
    pygame.image.save(img,"1.jpg")


    host = '95.2.11.146'
    port = 4999
    
    s = socket.socket()
    s.connect((host, port))
    filename = '1.jpg'

    with open(filename, 'rb') as f:
        bytesToSend = f.read(1024)
        s.send(bytesToSend)
        while bytesToSend != bytes(''.encode()):
            bytesToSend = f.read(1024)
            s.send(bytesToSend)

    s.close()
    

if __name__ == '__main__':
    Main()