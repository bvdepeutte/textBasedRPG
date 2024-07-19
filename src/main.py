import sys
import os
import pygame
from userCreation import characterCreation
from menu_game import MenuGame # from folder menu_system

DISPLAY_W,DISPLAY_H = 1280, 720
display = pygame.Surface((DISPLAY_W,DISPLAY_H))
window = pygame.display.set_mode(((DISPLAY_W,DISPLAY_H)))

menu_game = MenuGame(display,window,DISPLAY_W,DISPLAY_H)



while menu_game.running and menu_game.start_game == False:
    menu_game.curr_menu.display_menu()
    menu_game.game_loop()



#def main():
#    playercharacter = characterCreation()
#    playercharacter.selectLiveForm()
#    playercharacter.selectClass()
#    print("After some rest, you need a moment to come up with a plan based on your strengths and weaknesses")
#    playercharacter.selectTraits()

#if __name__ == "__main__":
#    main() 
