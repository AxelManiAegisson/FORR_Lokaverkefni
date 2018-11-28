import pygame
import random

width = 480
height = 580
FPS = 60

#litir
svart = (0,0,0)
hvitt = (255,255,255)
raudur = (255,0,0)


pygame.init()
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("Snake")
clock = pygame.time.Clock()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((15,15))
        self.image.fill(hvitt)
        self.rect = self.image.get_rect()
        self.rect.center = (width/2, height/2)
        self.x = width
        self.y = height
        self.hradi = 5

    def update(self):
        self.hradi = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.x = -self.hradi
        if keystate[pygame.K_RIGHT]:
            self.x = self.hradi
        if keystate[pygame.K_UP]:
            self.y = -self.hradi
        if keystate[pygame.K_DOWN]:
            self.y = self.hradi
        self.rect.x += self.hradi
        if self.rect.left > width:
            self.rect.right = 0
        if self.rect.right > width:
            self.rect.left = 0

class Epli(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((15,15))
        self.image.fill(raudur)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(width - self.rect.width)
        self.rect.y = random.randrange(height - self.rect.height)
        self.speed = 0


all_sprites = pygame.sprite.Group()
player = Player()
epli = Epli()
all_sprites.add(player)
all_sprites.add(epli)
#Loopa
keyra = True
while keyra:
    #Hraði
    clock.tick(FPS)
    #Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            keyra = False
    #Update
    all_sprites.update()
    #Teikning
    screen.fill(svart)
    all_sprites.draw(screen)
    #Eftir teikningu
    pygame.display.flip()

pygame.quit()
