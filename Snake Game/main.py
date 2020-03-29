import pygame
import random

STARTING_SPEED = 10
ACCELARATION = 1
# You don't really have to use this image though
# Can just draw a rect
# Which would make collision detection really easy :D
# SNAKE_PART_ICON = pygame.image.load("snake.png")
# Keeping this fixed for now
ALL_OBJECTS_WIDTH = 10
All_OBJECTS_HEIGHT = 10
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
# FOOD_IMAGE = pygame.image.load("food.png")
FPS = 30
SNAKE_COLOR = (255, 0, 0)
FOOD_COLOR = (0, 250, 0)

# score
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
running = True
icon = pygame.image.load("icon.png")
pygame.display.set_caption("Snake")
pygame.display.set_icon(icon)

score_value = 0
font = pygame.font.Font("freesansbold.ttf", 32)
textX = 10
textY = 10


snake = [(10, 50, ALL_OBJECTS_WIDTH, All_OBJECTS_HEIGHT)]
speed = STARTING_SPEED

velocity = (speed, 0)

# gameover
over_font = pygame.font.Font("freesansbold.ttf", 60)


def show_score(x, y):
    score = font.render("Score: " + str(score_value), True, (0, 125, 125))
    screen.blit(score, (x, y))


def game_over_text():
    over_text = over_font.render("GAME OVER", True, (200, 0, 100))
    screen.blit(over_text, (210, 250))


def generate_food_coordinates():
    return (
        random.randint(0 + ALL_OBJECTS_WIDTH, SCREEN_WIDTH
                       - ALL_OBJECTS_WIDTH),
        random.randint(0 + All_OBJECTS_HEIGHT, SCREEN_HEIGHT
                       - All_OBJECTS_HEIGHT),
        ALL_OBJECTS_WIDTH,
        All_OBJECTS_HEIGHT
    )


def draw_snake_part(coordinates):
    pygame.draw.rect(screen, SNAKE_COLOR, coordinates, 0)


def draw_food(coordinates):
    pygame.draw.rect(screen, FOOD_COLOR, coordinates, 0)


def has_collided_with_boundary(snake_head):
    return (
        snake_head[0] < 0
        or snake_head[0] + ALL_OBJECTS_WIDTH > SCREEN_WIDTH
        or snake_head[1] < 0
        or snake_head[1] + All_OBJECTS_HEIGHT > SCREEN_HEIGHT
    )


def has_collided(snake_head, obstacle):
    if snake_head[0] + ALL_OBJECTS_WIDTH < obstacle[0]:
        return False
    if snake_head[0] > obstacle[0] + ALL_OBJECTS_WIDTH:
        return False
    if snake_head[1] + All_OBJECTS_HEIGHT < obstacle[1]:
        return False
    if snake_head[1] > obstacle[1] + All_OBJECTS_HEIGHT:
        return False
    return True


def self_collision(snake):
    snake_head = snake[0]
    snake_body = snake[1:]
    if (len(snake) > 1):
        for snake_body_part in snake_body:
            if (snake_head[0] == snake_body_part[0]
                    and snake_head[1] == snake_body_part[1]):
                return True
        return False
    else:
        return False


def move_snake(snake, direction, elongate):
    new_snake = [move_snake_head(snake[0], direction)] + snake[:-1]
    if elongate:
        new_snake.append(snake[-1])
    return new_snake


def move_snake_head(snake, direction):
    return snake[0] + direction[0], snake[1] + direction[1],
    ALL_OBJECTS_WIDTH, All_OBJECTS_HEIGHT


food = generate_food_coordinates()
# Game loop
clock = pygame.time.Clock()
game_over = False
while running:

    if game_over:
        # No need to render anything now
        continue
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT and velocity[1] != 0:
                velocity = (speed, 0)
            elif event.key == pygame.K_LEFT and velocity[1] != 0:
                velocity = (-speed, 0)
            elif event.key == pygame.K_UP and velocity[0] != 0:
                velocity = (0, -speed)
            elif event.key == pygame.K_DOWN and velocity[0] != 0:
                velocity = (0, speed)

    if has_collided_with_boundary(snake[0]):
        game_over = True
        game_over_text()

    if has_collided(snake[0], food):
        food = generate_food_coordinates()
        score_value += 1
        snake = move_snake(snake, velocity, True)
        speed = speed + ACCELARATION
    else:
        snake = move_snake(snake, velocity, False)

    for snake_part in snake:
        draw_snake_part(snake_part)

    if self_collision(snake):
        game_over = True
        game_over_text()

    draw_food(food)
    show_score(10, 10)
    pygame.display.update()
    clock.tick(FPS)
