import pygame
import math
import random

pygame.init()
screen = pygame.display.set_mode((800, 600))
running = True
icon = pygame.image.load("icon.png")
pygame.display.set_caption("Snake")
pygame.display.set_icon(icon)
speed = 0.5

# score
score_value = 0
font = pygame.font.Font("freesansbold.ttf", 32)
textX = 10
textY = 10

# gameover
over_font = pygame.font.Font("freesansbold.ttf", 60)


def show_score(x, y):
    score = font.render("Score: " + str(score_value), True, (0, 125, 125))
    screen.blit(score, (x, y))


def game_over_text():
    over_text = over_font.render("GAME OVER", True, (200, 0, 100))
    screen.blit(over_text, (210, 250))


# snake
snakeImg = []
snakeX = []
snakeY = []
snakeX_change = []
snakeY_change = []
snakeImg.append(pygame.image.load("snake.png"))
snakeX.append(10)
snakeY.append(500)
snakeX_change.append(speed)
snakeY_change.append(0)
# snakeImg.append(pygame.image.load("snake.png"))
# snakeX.append(5)
# snakeY.append(500)
# snakeX_change.append(speed)
# snakeY_change.append(0)

# food
foodImg = pygame.image.load("food.png")
foodX = random.randint(15, 750)
foodY = random.randint(15, 550)


def snake(x, y, i):
    screen.blit(snakeImg[i], (x, y))


def food(x, y):
    screen.blit(foodImg, (x, y))


def boundry_check(x, y):
    if x == 0 or x == 770 or y == 0 or y == 660:
        return True
    else:
        return False


def distance(x, y, a, b):
    return (math.sqrt(math.pow((x-a), 2)+math.pow((y-b), 2)))


def isCollision():
    if distance(snakeX[0], snakeY[0], foodX, foodY) < 30:
        return True
    else:
        return False


def change():
    for i in range(len(snakeImg)-1):
        snakeX[i+1] = snakeX[i]
        snakeY[i+1] = snakeY[i]-30
        # snakeX_change[i+1]=snakeX_change[i]
        # snakeY_change[i+1]=snakeY_change[i]
# def change_2()
#   for i in range(len(snakeImg)-1)
#   if snakeX[i+1]==snake[i] and if snakeY[i+1]==snakeY[i]
#     snakeX_change[]


def snake_add():
    if len(snakeImg) > 1:
        if (snakeY[-1]-snakeY[-2]) == 0 and (snakeX[-1]-snakeX[-2]) > 0:
            snakeImg.append(pygame.image.load("snake.png"))
            snakeX.append(snakeX[-1])
            snakeY.append((snakeY[-1])-30)
        if (snakeY[-1]-snakeY[-2]) == 0 and (snakeX[-1]-snakeX[-2]) < 0:
            snakeImg.append(pygame.image.load("snake.png"))
            snakeX.append(snakeX[-1])
            snakeY.append((snakeY[-1])+30)
        if (snakeX[-1]-snakeX[-2]) == 0 and (snakeY[-1]-snakeY[-2]) > 0:
            snakeImg.append(pygame.image.load("snake.png"))
            snakeX.append((snakeX[-1]-30))
            snakeY.append((snakeY[-1]))
        if (snakeX[-1]-snakeX[-2]) == 0 and (snakeY[-1]-snakeY[-2]) < 0:
            snakeImg.append(pygame.image.load("snake.png"))
            snakeX.append((snakeX[-1]+30))
            snakeY.append((snakeY[-1]))

    if len(snakeImg) == 1:
        if snakeX_change[0] == 0 and snakeY_change[0] > 0:
            snakeImg.append(pygame.image.load("snake.png"))
            snakeX.append(snakeX[-1])
            snakeY.append((snakeY[-1])-30)

        if snakeX_change[0] == 0 and snakeY_change[0] < 0:
            snakeImg.append(pygame.image.load("snake.png"))
            snakeX.append(snakeX[-1])
            snakeY.append((snakeY[-1])+30)

        if snakeY_change[0] == 0 and snakeX_change[0] > 0:
            snakeImg.append(pygame.image.load("snake.png"))
            snakeX.append(snakeX[-1]-30)
            snakeY.append((snakeY[-1]))

        if snakeY_change[0] == 0 and snakeX_change[0] < 0:
            snakeImg.append(pygame.image.load("snake.png"))
            snakeX.append(snakeX[-1]+30)
            snakeY.append((snakeY[-1]))


# Game loop
while running:
    screen.fill((255, 255, 255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT and snakeY_change[0] != 0:
                # change()
                snakeX_change[0] = speed
                snakeY_change[0] = 0

            if event.key == pygame.K_LEFT and snakeY_change[0] != 0:
                # change()
                snakeX_change[0] = -speed
                snakeY_change[0] = 0

            if event.key == pygame.K_UP and snakeX_change[0] != 0:
                # change()
                snakeX_change[0] = 0
                snakeY_change[0] = -speed

            if event.key == pygame.K_DOWN and snakeX_change[0] != 0:
                # change()
                snakeX_change[0] = 0
                snakeY_change[0] = speed

    if boundry_check(snakeX[0], snakeY[0]):
        for i in range(len(snakeImg)):

            snakeX_change[0] = 0
            snakeY_change[0] = 0
            game_over_text()

    if isCollision():
        foodX = random.randint(15, 750)
        foodY = random.randint(15, 550)
        score_value += 1
        snake_add()
        # change()

    snakeX[0] += snakeX_change[0]
    snakeY[0] += snakeY_change[0]

    for j in range(len(snakeImg)):

        # change()
        snake(snakeX[j], snakeY[j], j)
    # change()

    print(len(snakeImg))
    print(snakeX[:])
    print(snakeY[:])
    show_score(textX, textY)
    food(foodX, foodY)
    # change()
    pygame.display.update()
    # change()
