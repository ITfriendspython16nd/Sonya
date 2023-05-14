import pygame
from copy import deepcopy
from bullet import Bullet


pygame.init()
w, h = 600, 600
x, y = 0, 0
size = (w, h)
red = (255,0,0)
black = (0, 0, 0)
screen = pygame.display.set_mode(size)
right = False # 4
left = False # 3

player_left = pygame.image.load(f'right.png')
player_right = pygame.image.load(f'stand.png')
player_stand = pygame.image.load(f'left.png')

img = pygame.image.load(f'bg.png')

shoot = False # 8

bullet_x = 0
bullet_y = 0

direction = []



run = True
while run:
    screen.fill(red)
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    y -= ( h/20)*5
                if not shoot: #
                    if event.key == pygame.K_SPACE:
                        bullet_x, bullet_y = deepcopy(x)+30, deepcopy(y)
                        shoot =True #

    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= 1
        left = True
        right = False
    if keys[pygame.K_RIGHT]:
        x += 1
        left = False
        right = True

    if left:
        screen.blit(player_left, (x, y))
    elif right:
        screen.blit(player_right, (x, y))
    else:
        screen.blit(player_right, (x, y))
        
            
    s = pygame.Rect(x, y,30, 30)
    pygame.draw.rect(screen, black,s)

    if shoot:
        if left or right:
            direction.append((left, right))
        else:
            shoot = False
            direction.clear()

        if bullet_x <= 0 or bullet_x >= w:
            shoot = False
            direction.clear()

        if direction:
            if direction[0][0]:
                bullet_x -= 2
                bullet_y += 0.1
            elif direction[0][1]:
                bullet_x += 2
                bullet_y += 0.1
                
        bullet1 = Bullet(bullet_x, bullet_y, 'bullet.png')
        screen.blit(bullet1.image, bullet1.rect)


    pygame.display.flip()