import pygame
import pygame_gui
import sys
import time
from userCreation import characterCreation
class Game():
    def __init__(self,display,window,display_w,display_h):
        self.display = display
        self.window = window
        self.DISPLAY_W = display_w
        self.DISPLAY_H = display_h
        self.font_name = pygame.font.get_default_font()
        self.BLACK, self.WHITE, self.RED = (0, 0, 0), (255, 255, 255), (122, 38, 58)
        self.text_size = 20
        self.timer = pygame.time.Clock()
        self.playing = True

    def blit_screen(self):
        self.window.blit(self.display, (0, 0))
        pygame.display.update()

    def game_loop(self):
        print('enter the loop')
        while self.playing:
            print(self.playing)
            self.display.fill(self.BLACK)
            self.blit_screen()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    print("quit")
                    pygame.quit()
                    sys.exit()
            self.draw_text_game("this is a very veryveryveryveryveryveryveryveryveryveryveryvery text",self.text_size,self.DISPLAY_W/2,self.DISPLAY_H/2)
            self.window.blit(self.display,(0,0))
            pygame.display.update()
            time.sleep(10)

            #playercharacter = characterCreation()
            #playercharacter.selectLiveForm()
            #playercharacter.selectClass()
            #print("After some rest, you need a moment to come up with a plan based on your strengths and weaknesses")
            #playercharacter.selectTraits()



    def draw_text_game(self, text, size, x, y,fontColor=None,backgroundColor=None):
        font = pygame.font.Font(self.font_name,size)
        fontColor = fontColor or self.WHITE
        message = text
        print(message)
        snip = font.render("", True, fontColor)
        counter = 0
        speed = 100
        done = False    
        while counter < len(message) * speed:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            counter += 1

            snip = font.render(message[0:counter//speed], True, fontColor, backgroundColor)
            print(message[0:counter//speed])
            if backgroundColor:
                text_rect = snip.get_rect(topleft=(x, y))
                self.display.fill(backgroundColor, text_rect)

            self.window.blit(snip, (x, y))
            pygame.display.flip()
            
    def draw_fix_text(self, text, size, x, y,fontColor=None,backgroundColor=None):
        font = pygame.font.Font(self.font_name,size)
        fontColor = fontColor or self.WHITE
        text_surface = font.render(text, True, fontColor)
        original_text_rect = text_surface.get_rect()
        extended_text_rect = pygame.Rect(0, 0, original_text_rect.width + 10, original_text_rect.height + 6)
        extended_text_rect.center = (x, y)
        if backgroundColor:
            pygame.draw.rect(self.display, backgroundColor, extended_text_rect,0,7,7,7,7,7)
        text_surface_rect = text_surface.get_rect(center=extended_text_rect.center)
        self.display.blit(text_surface,text_surface_rect)