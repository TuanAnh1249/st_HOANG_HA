import pygame
import sys
pygame.init
# chieu dai chieu rong
width , height = 800, 450
# khai bao khung tro choi
scr = pygame.display.set_mode((width,height))
bg =pygame.image.load('./img/bg.jpg')
bg=pygame.transform.scale(bg,(width,height))
character=pygame.image.load('./img/character.jpg')
character=pygame.transform.scale(character,(200,180))
character_rect=character.get_rect(center=(400,225))


while True: 
    for event in pygame.event.get():   #lay su kien trong pyagme
        if event.type == pygame.QUIT:   #so sanh voi gia tri thoat
            pygame.quit()
            sys.exit()
    scr = pygame.display.set_mode((width,height))
    scr.blit(bg,(0,0))
    scr.blit(character,character_rect)
    pygame.display.update()

