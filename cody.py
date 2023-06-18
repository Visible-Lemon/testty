import pygame
import random

# Initialize Pygame
pygame.init()

# Window dimensions
window_width = 400
window_height = 400

# Snake and food dimensions
snake_size = 20
food_size = 20

# Colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

# Create the game window
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('Snake Game')

clock = pygame.time.Clock()
snake_speed = 10

# Font for displaying the score
font_style = pygame.font.SysFont(None, 30)


def display_score(score):
    score_text = font_style.render("Score: " + str(score), True, white)
    window.blit(score_text, [10, 10])


def draw_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(window, black, [x[0], x[1], snake_block, snake_block])


def game_loop():
    game_over = False
    game_quit = False

    # Initial position of the snake
    x1 = window_width / 2
    y1 = window_height / 2

    # Change in position
    x1_change = 0
    y1_change = 0

    # Initialize the snake
    snake_list = []
    snake_length = 1

    # Position the food randomly
    food_x = round(random.randrange(0, window_width - food_size) / 20.0) * 20.0
    food_y = round(random.randrange(0, window_height - food_size) / 20.0) * 20.0

    while not game_quit:
        while game_over:
            window.fill(black)
            game_over_text = font_style.render("Game Over! Press Q-Quit or C-Play Again", True, white)
            window.blit(game_over_text, [window_width / 6, window_height / 3])
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_quit = True
                    game_over = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_quit = True
                        game_over = False
                    if event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_quit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_size
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_size
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_size
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_size
                    x1_change = 0

        # Check if the snake hits the window boundaries
        if x1 >= window_width or x1 < 0 or y1 >= window_height or y1 < 0:
            game_over = True

        x1 += x1_change
        y1 += y1_change
        window.fill(black)
        pygame.draw.rect(window, red, [food_x, food_y, food_size, food_size])
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append

#this code is ready for works....
