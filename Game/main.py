import pygame
import random
#Initialize the Pygame
pygame.init()
#Create the Screen
screen=pygame.display.set_mode((800,600))
running=True
# Title and Icon
pygame.display.set_caption("Space Innvaders")
icon= pygame.image.load("ufo.png")
pygame.display.set_icon(icon)

#Background
background = pygame.image.load("background.png")

#Player
playerImg=pygame.image.load("space_invaders.png")
playerX=370
playerY=480 

#Enemy
enemyImg=pygame.image.load("alien.png")
enemyX=random.randint(0,800)
enemyY=random.randint(50,150)

#Bullet
bulletImg=pygame.image.load("bullet.png")
bulletX=0
bulletY=480

#Variable for change
playerX_change=0
enemyX_change=4
enemyY_change=40
bulletY_change=10
bullet_state="ready"

def player(x,y):
    screen.blit(playerImg, (x,y))

def enemy(x,y):
    screen.blit(enemyImg,(x,y))

def fire_bullet(x,y):
    global bullet_state
    bullet_state="fire"
    screen.blit(bulletImg,(x+16,y+10))
#game loop
while running:
    screen.fill((0,0,0))
    screen.blit(background,(0,0))
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running= False
    # Keyboard input
        if event.type== pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                playerX_change = -5
            if event.key==pygame.K_RIGHT:
               playerX_change = 5
            if event.key==pygame.K_SPACE:
                if bullet_state == "ready":
                    bulletX=playerX
                    fire_bullet(bulletX,bulletY)    
        if event.type==pygame.KEYUP:
            if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
                playerX_change = 0
        
    
    playerX +=playerX_change
    if playerX <= 0:
            playerX=0
    elif playerX >= 736:
             playerX=736   

    enemyX +=enemyX_change
    if enemyX <= 0:
            enemyX_change=4
            enemyY += enemyY_change
    elif enemyX >= 736:
             enemyX_change=-4    
             enemyY += enemyY_change     
    player(playerX,playerY)
    enemy(enemyX,enemyY)
    
   # Bullet Movement
    if bulletY <= 0:
        bulletY = 480
        bullet_state="ready" 
    if bullet_state == "fire":
        fire_bullet(bulletX,bulletY)
        bulletY-=bulletY_change
   
     
    pygame.display.update()
