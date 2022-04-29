import pygame
from snake_classes1 import *
import json
from snake_main1 import *
s = input("Hello! Who are you")
name = s
mini_data[s] = 0
if s not in f.keys():
    f[s] = 0
    print("You are registered")
"""data_snake_read.close()
data_snake_write.close()
data_snake_read = open('snake_data.json', 'r')
data_snake_write = open('snake_data.json', 'w')"""
#json.dump(f, data_snake_write)
s = input("Ok. What do you want? 'play', 'statistics'")

menu(name, s)