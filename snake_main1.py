from random import choice
import random
import os
import pygame
from pygame.locals import *
from snake_classes1 import *
from insert_into_data_snake import data_insert, data_get, data_show
# import json
# data_snake_read = open('snake_data.json', 'r')
# f = json.load(data_snake_read)
# data_snake_write = open('snake_data.json', 'w')

mini_data = {}
pause = False
def main_menu(name, s):
    pygame.init()
    new_player = False
    if name == '':
        new_player = True
    screen = pygame.display.set_mode((400, 200))
    font = pygame.font.Font(None, 32)
    clock = pygame.time.Clock()
    input_box = pygame.Rect(100, 100, 140, 32)
    color_inactive = pygame.Color('lightskyblue3')
    color_active = pygame.Color('dodgerblue2')
    color = color_inactive
    active = False
    text = ''
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    done = True
                    play(text, s)
                    text = ''
                elif event.key == pygame.K_BACKSPACE:
                    text = text[:-1]
                else:
                    text += event.unicode

        screen.fill((30, 30, 30))
        # Render the current text.
        txt_surface = font.render(text, True, color)
        hello = font.render("Hello! Who Are You?", True, color)
        hello_again = font.render("Do You Want to Play Again?", True, color)
        # Resize the box if the text is too long.
        width = max(200, txt_surface.get_width() + 10)
        input_box.w = width
        screen.blit(txt_surface, (input_box.x + 5, input_box.y + 5)) # Show The Text What You Have Written
        if new_player:
            screen.blit(hello, (input_box.x, input_box.y - 30))  # Introduction
        else:
            screen.blit(hello_again, (input_box.x -40, input_box.y - 30))  # Continue
        pygame.draw.rect(screen, color, input_box, 2)
        pygame.display.flip()
        clock.tick(30)
def play(name, s):
    global pause
    global f
    global mini_data
    global wall_positions
    global sequence
    global size
    global WIDTH
    global HEIGHT


    pygame.init()

    font = pygame.font.SysFont('comicans', 30, True, False)
    font_large = pygame.font.SysFont('comicans', 100, True, False)
    BACKGROUND = pygame.transform.scale(pygame.image.load('Grass.png'), (720, 720))
    pygame.init()
    RED = (255, 0, 0)
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    Score = 0
    m = 0

    speed = 25

    SONG_END = pygame.USEREVENT + 1
    pygame.mixer.music.set_endevent(SONG_END)

    PW1 = PreWall(440, 70)
    PW2 = PreWall(290, 70)
    PW3 = PreWall(380, 70)
    PW4 = PreWall(440, 500)
    PW5 = PreWall(120, 200)
    PW6 = PreWall(450, 120)
    PW7 = PreWall(400, 300)
    PW8 = PreWall(350, 230)
    W11 = Wall(120, 70)
    W22 = Wall(190, 70)
    W33 = Wall(300, 70)
    W1 = Wall(440, 70)
    W2 = Wall(290, 70)
    W3 = Wall(380, 70)
    W4 = Wall(440, 500)
    W5 = Wall(120, 200)
    W6 = Wall(450, 120)
    W7 = Wall(400, 300)
    W8 = Wall(350, 230)
    A = Apple()
    k = [W1, W2, W3, W4, W5, W6, W7]
    S = Snake()
    prewalls = [PW1, PW2, PW3, PW4, PW5, PW6, PW7, PW8]
    apple = pygame.sprite.Group()
    walls = pygame.sprite.Group()
    player = pygame.sprite.Group()
    walls.add(W11, W22, W33)
    player.add(S)
    apple.add(A)
    running = True
    screen = pygame.display.set_mode(size)
    screen.fill((255, 255, 255))
    pygame.display.set_caption('Snake')
    clock = pygame.time.Clock()
    while running:
        # SNAKE SNAKE CONTROL
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == KEYDOWN:
                if event.key == K_RETURN:
                    pause = not pause
                if event.key == K_ESCAPE:
                    running = False
                if (event.key == K_UP or event.key == K_w) and S.direction != (0, 15) and event.key != K_DOWN:
                    S.direction = (0, -15)
                if (event.key == K_DOWN or event.key == K_s) and S.direction != (0, -15) and event.key != K_UP:
                    S.direction = (0, 15)
                if (event.key == K_RIGHT or event.key == K_d) and S.direction != (-15, 0) and event.key != K_LEFT:
                    S.direction = (15, 0)
                if (event.key == K_LEFT or event.key == K_a) and S.direction != (15, 0) and event.key != K_RIGHT:
                    S.direction = (-15, 0)

        screen.blit(BACKGROUND, (0, 20)) # The Grass where the snake is going
        pygame.draw.rect(screen, pygame.Color('lime'), (0, 0, WIDTH, 20)) # The Score View
        for i in apple: # Draw The Apple(Food)
            i.draw(screen)
        for i in walls:  # Draw Walls
            i.draw(screen)
        # for i in prewalls:
        # i.draw(screen)
        if not pause:
            S.move(screen) # Snake's Moving
        else:
            S.draw(screen)
        # THE LOGIC OF EATING
        if pygame.sprite.spritecollideany(S, apple):
            m = Score // 5 # Counter of Levels
            for i in apple: # Change The Position of The Apple
                i.move(screen)
                while pygame.sprite.spritecollideany(S, apple) or pygame.sprite.spritecollideany(i, walls): # Change The Position of The Apple If The Apple stays in The Wall
                    i.move(screen)
            for i in walls:
                i.move(screen)
            S.eat_apple(screen) # The Snake Becomes Longer
            Score += random.randint(1, 3)  # Points How More Scores Snake Gets If It Eats The Apple
            if m != Score // 5 and m < len(k): # Add Walls If Level Is Increased
                walls.add(k[m])
        # SHOW THE SCORE AND RANK
        pygame.draw.rect(screen, ((250, 200, 30)), (720, 20, 280, 900)) # The Score View
        screen.blit(font.render(f'Statistics', True, ((0,0,0))), (740, 75))  # Show The Scores
        data_show(screen, 740, 100) # Show The Data
        screen.blit(font.render(f'Score:{Score}         Level:{Score // 5}', True, WHITE), (0, 0)) # Show The Scores
        # for i in range(10):
        #     screen.blit(font.render(f'Arslan', True, WHITE), (i*10, 200))
        speed = 10 + (Score // 5) * 2
        if S.rect.x < 2.5 or S.rect.x + 17.5 > 720 or S.rect.y < 10 or S.rect.y + 17.5 > HEIGHT or S.rect.center in S.body or pygame.sprite.spritecollideany(
                S, walls): # Stop The Game If The Snake Goes Out of The Grass Or Collides With Walls
            pygame.mixer.music.stop()
            screen.fill((111, 111, 111))
            screen.blit(font_large.render(f'GAME OVER!', True, WHITE), (210, 100))
            screen.blit(font.render(f'Yor score: {Score}', True, WHITE), (390, 180))
            screen.blit(font.render(f'Level:{Score // 5}', True, WHITE), (410, 210))
            pygame.display.update()
            pygame.time.delay(3000)
            running = False
        if pause:
            clock.tick(10)
        else:
            clock.tick(speed)
        pygame.display.flip()
    pygame.quit()
    pygame.init()
    data_insert(name, Score // 5)
    main_menu(name, s)
main_menu('', '')


