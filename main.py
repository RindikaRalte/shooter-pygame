import pygame
import random 

pygame.init()

screen = pygame.display.set_mode((800,600))
background = pygame.image.load('background.jpg')
resize_background = pygame.transform.scale(background,(800,600))

playerIMG = pygame.image.load('spaceship.png')
playerX = 350
playerY = 400

reszie_player = pygame.transform.scale(playerIMG,(100,100))

enemyIMG = pygame.image.load('bird.png')
enemyX = random.randint(0,800)
enemyY = random.randint(0,50)
enemy_speed = 10
enemyY_upDown = 10

bullet = pygame.image.load('laser.png')
bulletX = 350
bulletY = 400
bulletY_speed = 0.5
bullet_state = "ready"

resize_bullet = pygame.transform.scale(bullet,(20,60))

game_over = False

def bullet():
    global bulletX, bulletY, bulletY_speed, bullet_state, enemyX, enemyY, playerX, playerY,reszie_bullet
    if bullet_state == "ready":
        bullet_state = "fire"
        bulletX = playerX + 40  
        bulletY = playerY - 45
    
    if bullet_state == "fire":
        screen.blit(resize_bullet, (bulletX, bulletY))
        bulletY -= bulletY_speed

        bullet_rect = resize_bullet.get_rect(topleft=(bulletX, bulletY))
        enemy_rect = resize_enemy.get_rect(topleft=(enemyX, enemyY)) 

        if bullet_rect.colliderect(enemy_rect):
            bullet_state = "ready"
            enemyX = random.randint(0, 800)
            enemyY = random.randint(0, 50)

        if bulletY <= 0:
            bullet_state = "ready"
            bulletY = playerY
    
    

    

resize_enemy = pygame.transform.scale(enemyIMG,(80,80))
def enemy():


    screen.blit(resize_enemy,(enemyX,enemyY))


def player():
    screen.blit(reszie_player,(playerX,playerY))

def game_over_check():
    global playerX,playerY,enemyX,enemyY,game_over
    player_rect = reszie_player.get_rect(topleft = (playerX,playerY))
    enemy_rect = resize_enemy.get_rect(topleft=(enemyX, enemyY))

    if player_rect.colliderect(enemy_rect):
        game_over = True
    

running = True

while running:
    screen.fill((0,0,0))
    screen.blit(resize_background,(0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and playerX >  0:
        playerX -= 2
    if keys[pygame.K_RIGHT] and playerX < 800-100:
        playerX += 2
    if keys[pygame.K_SPACE]:
        bullet()
    
     
    enemyX += enemy_speed
    if enemyX <= 0 or enemyX > 800-80:
        enemy_speed = -enemy_speed
        enemyY += enemyY_upDown
    
    if game_over:
        font = pygame.font.Font(None, 74)
        text = font.render('GAME OVER', True,(255,0,0))
        screen.blit(text,(200,250))


    game_over_check()
    player()
    enemy()
    pygame.display.update()