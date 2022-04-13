import pygame.camera
import pygame.image
from pygame.locals import *

pygame.camera.init()
pygame.init()

cameras = pygame.camera.list_cameras()

print("Using camera %s ..." % cameras[0])

cam1 = pygame.camera.Camera(cameras[0])
cam1.start()

img1 = cam1.get_image()

size = width, height = 640,480

screen = pygame.display.set_mode((size))
pygame.display.set_caption("Camera")

while 1:
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            pygame.quit()

    img1 = cam1.get_image()

    screen.blit(img1, (0, 0))

    pygame.display.update()
