import pygame
from random import randint

pygame.init()

w, h = 500, 500
win = pygame.display.set_mode((w, h))
pygame.display.set_caption('Звёздное Небо')
FPS = 150
clock = pygame.time.Clock()


win.fill((0, 0, 0))

while True:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            exit()

    #win.fill((0, 0, 0))

    button = pygame.mouse.get_pressed()
    if button[0]:
        pos = pygame.mouse.get_pos()
        pygame.draw.circle(win, (255, 255, 255), pos, 5)

    pygame.draw.circle(win, (122, 122, 122), (randint(0, 500), randint(0, 500)), 1)

    pygame.display.update()

    clock.tick(FPS)
        