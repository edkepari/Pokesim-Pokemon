import pygame, sys
from pygame.locals import *
from time import sleep, time

pygame.init()
pygame.mixer.init()


width,height = 800,600
screen=pygame.display.set_mode((width,height))


#HealthBar related initializations
healthbar = ("healthbar.png")
hb= pygame.image.load(healthbar).convert_alpha()
health = ("health.png")
h = pygame.image.load(health).convert_alpha()

healthvalue = 200

gameloop = True

font= pygame.font.Font(None, 45)
LossMsg= font.render("YOU LOST", True, (255,255,255))
while gameloop==True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameloop = False 
    pygame.display.flip()
    screen.blit(hb, (5,5))
    screen.blit(hb, (595,495))
    for health1 in range(healthvalue):
        screen.blit(h, (health1+5,8))
        screen.blit(h, (health1+595,498))
    '''screen.blit(HP,  (50, 25))'''
    healthvalue-=1
    
    if healthvalue<=0:
        screen.blit(LossMsg, (300,300))
    sleep(0.01)

