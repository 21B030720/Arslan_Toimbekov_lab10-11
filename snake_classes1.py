from random import choice
import os
import pygame
import random
#from Snake_yy import *
from pygame.locals import *
mini_data = []
wall_positions = [(120, 70), (190, 70), (300, 70), (440, 70), (290, 70), (380, 70), (440, 500), (120, 200), (450, 120), (400, 300), (350, 230)]
sequence = [7.5 + 15*i for i in range(1,48)]
size = WIDTH, HEIGHT = (920,740)
class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.x, self.y = x, y
        self.image = pygame.image.load("snake_wall.png")
        self.image = pygame.transform.scale(self.image, (90, 70))
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)
    def move(self, Screen):
        self.draw(Screen)
    def draw(self, Screen):
        Screen.blit(self.image, self.rect)

class PreWall():
    def __init__(self, x, y):
        super().__init__()
        self.x, self.y = x, y
    def draw(self, Screen):
        self.image = pygame.draw.rect(Screen, (0, 255, 0), pygame.Rect(self.x, self.y, 90, 70), 0)
        #Screen.blit(self.image, )
class Apple(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("snake_apple.png")
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.rect = self.image.get_rect()
        self.rect.center = (300, 400)
    def move(self, Screen):
        m = (random.randint(200, 600), random.randint(200, 600))
        self.rect.center = m
        self.draw(Screen)
    def draw(self, Screen):
        Screen.blit(self.image, self.rect)

class Snake(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.body = []
        self.image = pygame.transform.scale(pygame.image.load('snake_head.png'), (30, 30))
        self.im_of_body = pygame.transform.scale(pygame.image.load('snake_body.png'), (30, 30))
        self.rect = self.image.get_rect(center=(WIDTH / 2 - 7.5, 10 + HEIGHT / 2 - 7.5))
        self.direction = (15, 0)
        self.save_direction = (15, 0)
        self.save = True

    def move(self, screen):
        for i in range(len(self.body) - 1):
            self.body[i] = self.body[i + 1]
            screen.blit(self.im_of_body, self.im_of_body.get_rect(center=self.body[i]))
        if self.body:
            self.body[-1] = (self.rect.center)
            screen.blit(self.im_of_body, self.im_of_body.get_rect(center=self.body[-1]))
        self.rect.move_ip(self.direction)
        screen.blit(pygame.transform.rotate(self.image, ({1: 0, 0: 0, -1: 1}[self.direction[1] / 15]) * (180) + (
                    self.direction[0] / 15) * 90), self.rect)
    def draw(self, screen):
        screen.blit(pygame.transform.rotate(self.image, ({1: 0, 0: 0, -1: 1}[self.direction[1] / 15]) * (180) + (
                self.direction[0] / 15) * 90), self.rect)

    def eat_apple(self, screen):
        self.body.append((-20, -20))

