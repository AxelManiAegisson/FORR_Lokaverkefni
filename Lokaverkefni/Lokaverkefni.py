import pygame
import random

width = 800
height = 600
FPS = 60

#litir
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)

pygame.init()
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("Snake")
clock = pygame.time.Clock()

lead_x = 400
lead_y = 300
lead_x_change = 0
lead_y_change = 0
gameExit = False
while not gameExit:
    #Hraði
    clock.tick(FPS)
    #Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                lead_x_change -= 5
                lead_y_change = 0
            elif event.key == pygame.K_RIGHT:
                lead_x_change = 5
                lead_y_change = 0
            elif event.key == pygame.K_DOWN:
                lead_y_change = 5
                lead_x_change = 0
            elif event.key == pygame.K_UP:
                lead_y_change -= 5
                lead_x_change = 0
        if lead_x >= width:
            lead_x = 0
        elif lead_x <= 0:
            lead_x = width
        


    #Update
    lead_x += lead_x_change
    lead_y += lead_y_change
    #Teikning
    screen.fill(black)
    pygame.draw.rect(screen,white,[lead_x,lead_y,10,10])
    #Eftir teikningu
    pygame.display.flip()

pygame.quit()
