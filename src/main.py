import sys
import os
import pygame
from menu_game import MenuGame # from folder menu_system
from game import Game
pygame.init()

DISPLAY_W,DISPLAY_H = 1280, 720
display = pygame.Surface((DISPLAY_W,DISPLAY_H))
window = pygame.display.set_mode(((DISPLAY_W,DISPLAY_H)))

menu_game = MenuGame(display,window,DISPLAY_W,DISPLAY_H)
game = Game(display,window,DISPLAY_W,DISPLAY_H)


while menu_game.running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            menu_game.running = False
    menu_game.curr_menu.display_menu()
    if menu_game.playing:
        game.game_loop()