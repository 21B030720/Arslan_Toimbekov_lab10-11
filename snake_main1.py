from random import choice
import random
import os
import pygame
from pygame.locals import *
from snake_classes1 import *
import json
data_snake_read = open('snake_data.json', 'r')
f = json.load(data_snake_read)
data_snake_write = open('snake_data.json', 'w')

mini_data = {}

def play(name, s):
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
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == KEYDOWN:
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

        screen.blit(BACKGROUND, (0, 20))
        pygame.draw.rect(screen, pygame.Color('lime'), (0, 0, WIDTH, 20))
        for i in apple:
            i.draw(screen)
        for i in walls:
            i.draw(screen)
        # for i in prewalls:
        # i.draw(screen)
        S.move(screen)
        if pygame.sprite.spritecollideany(S, apple):
            m = Score // 5
            for i in apple:
                i.move(screen)
                while pygame.sprite.spritecollideany(S, apple) or pygame.sprite.spritecollideany(i, walls):
                    i.move(screen)
            for i in walls:
                i.move(screen)
            S.eat_apple(screen)
            Score += random.randint(1, 3)  #########
            if m != Score // 5 and m < len(k):
                # prewalls = prewalls[1:]
                walls.add(k[m])
        screen.blit(font.render(f'Score:{Score}         Level:{Score // 5}', True, WHITE), (0, 0))
        speed = 10 + (Score // 5) * 2
        if S.rect.x < 2.5 or S.rect.x + 17.5 > WIDTH or S.rect.y < 10 or S.rect.y + 17.5 > HEIGHT or S.rect.center in S.body or pygame.sprite.spritecollideany(
                S, walls):
            pygame.mixer.music.stop()
            screen.fill((111, 111, 111))
            screen.blit(font_large.render(f'GAME OVER!', True, WHITE), (100, 100))
            screen.blit(font.render(f'Yor score: {Score}', True, WHITE), (250, 180))
            screen.blit(font.render(f'Level:{Score // 5}', True, WHITE), (270, 210))
            pygame.display.update()
            pygame.time.delay(3000)
            running = False
        clock.tick(speed)
        pygame.display.flip()
    #global mini_data
    """if mini_data[name] < Score // 5:
        mini_data[name] = Score // 5"""
    if f[name] < Score // 5:
        f[name] = Score // 5
    pygame.quit()
    pygame.init()
    menu_continuous(name, s)
def menu_continuous(name, s):
    global f
    s = input("Well, do want to try again?")
    if s == 'yes':
        play(name, s)
        pygame.quit()
    elif s == 'no':
        s = input('Do you want to see statistics?')
        if s == 'yes':
            #lobal f
            f_sorted = dict(sorted(f.items(), key=lambda x: x[1], reverse = True))
            f = f_sorted
            print(f)
            json.dump(f, data_snake_write)
            data_snake_read.close()
            data_snake_write.close()
        elif "no":
            #global f
            f_sorted = dict(sorted(f.items(), key=lambda x: x[1], reverse = True))
            f = f_sorted
            print("Thank you for attention! Good bye!")
            json.dump(f, data_snake_write)
            data_snake_read.close()
            data_snake_write.close()
            pygame.quit()
def menu(name, s):
    if s == "play":
        print("Ok")
        play(name, s)

