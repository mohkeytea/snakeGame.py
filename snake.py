import pygame
import time
import random

pygame.init()

# define colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)

# set the window size
window_width = 600
window_height = 400

# create the game window
game_display = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('Snake Game')

# set the game clock
clock = pygame.time.Clock()

# set the font for displaying the score
font_style = pygame.font.SysFont(None, 30)


def display_score(score):
    score_text = font_style.render("Score: " + str(score), True, white)
    game_display.blit(score_text, [0, 0])


def draw_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(game_display, green, [x[0], x[1], snake_block, snake_block])


def message(msg, color):
    msg_text = font_style.render(msg, True, color)
    game_display.blit(msg_text, [window_width/6, window_height/3])


def game_loop():
    # set the game variables
    game_over = False
    game_close = False

    # set the snake variables
    snake_block = 10
    snake_speed = 15
    x1 = window_width / 2
    y1 = window_height / 2
    x1_change = 0
    y1_change = 0
    snake_list = []
    length_of_snake = 1

    # set the food variables
    foodx = round(random.randrange(0, window_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, window_height - snake_block) / 10.0) * 10.0

    # start the game loop
    while not game_over:

        while game_close:
            game_display.fill(black)
            message("You Lost! Press Q-Quit or C-Play Again", red)
            display_score(length_of_snake - 1)
            pygame.display.update()

            # handle key events
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        # check if the snake hits the walls
        if x1 >= window_width or x1 < 0 or y1 >= window_height or y1 < 0:
            game_close = True

        # update the snake position
        x1 += x1_change
        y1 += y1_change

        # clear the game display
        game_display.fill(black)
        
        #Draw the food
        pygame.draw.rect(game_display,red, [foodx, foody, snake_block, snake_block])
        
        #update the snake's head position
        snake-head = []
        snake-head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)
        
        #Remove the tail if the snake exceeds its length
        if len(snake_list) > length_of_snake:
               del snake_list[0]
                
        #check if the snake collides with itself
        for x in snake_list[:-1]:
            if x ==snake-head:
                game_close = True
                
        # Draw the snake
        draw_snake(snake_block, snake-list)
        
        #Display the score
        display_score(length_of_snake -1)
        
         #update the game display
            pygame.display.update()
            
         # check if the snake eats the food
         if x1 == foodx and y1 == foody:
                foodx = round(random.randrange(0, window_width - snake_block) / 10.0) * 10.0
                    foody = round(random.randrange(0, window_height - snake_block) /10.0) * 10.0
                    length_of_snake += 1
                    
         # set the game speed
        clock.tick(snake_speed)
        
       # Quit the game
    pygame.quit()
    quit()
    
   # start the game loop
game_loop()
        
