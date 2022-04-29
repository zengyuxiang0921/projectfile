import pygame
import pygame.camera
import time
import os
main_run=True
times=0
while main_run:
    if __name__ == '__main__':
        width = 640
        height = 480
        times +=1
        display = pygame.display.set_mode((width, height))
        pygame.init()
        pygame.camera.init()
        cam_list = pygame.camera.list_cameras()
        cam = pygame.camera.Camera(cam_list[0], (width, height))
        cam.start()
        time.sleep(1)
        img = cam.get_image()
        cam.stop()
        display.blit(img, (0, 0))
        preview = True
        while preview:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit(0)
                if event.type== pygame.KEYDOWN:
                    if event.key == pygame.K_e:
                        exit(0)
                    else:
                        preview = False
                pygame.display.update()
                pygame.display.flip()

        if not os.path.exists("camera picture"):
            os.mkdir("camera picture")
        pygame.image.save(img, os.path.join("camera picture", "camera img({}).bmp".format(times)))