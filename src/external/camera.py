#Camera acess with PI
import cv2

class Camera:
    def __init__(self):
        pass

    #current testing phase TODO
    def capture_image(self):
        img = cv2.imread('img2.jpg',0)
        return img