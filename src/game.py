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
        self.title = 50
        self.subtitle = 35
        self.timer = pygame.time.Clock()
        self.playing = True
        self.SPACE_KEY, self.UP_KEY, self.DOWN_KEY = False, False, False



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
            self.window.blit(self.display,(0,0))
            pygame.display.update()
            self.timer.tick(30)
            self.draw_fix_text("The Project:", self.title, self.DISPLAY_W/2, 70, self.WHITE, self.RED)
            self.draw_fix_text("A text based RPG",self.subtitle, self.DISPLAY_W/2, 140, self.WHITE)
            self.draw_text_game("A text based RPG",self.subtitle, 10, 200, self.WHITE)
            self.draw_fix_text("Press space to continue",self.text_size,self.DISPLAY_W /2, self.DISPLAY_H - 60)
            self.wait_for_space_bar()


            #playercharacter = characterCreation()
            #playercharacter.selectLiveForm()
            #playercharacter.selectClass()
            #print("After some rest, you need a moment to come up with a plan based on your strengths and weaknesses")
            #playercharacter.selectTraits()

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False, False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.SPACE_KEY = True
                if event.key == pygame.K_DOWN:
                    self.DOWN_KEY = True
                if event.key == pygame.K_UP:
                    self.UP_KEY = True

    def reset_keys(self):
        self.UP_KEY, self.DOWN_KEY, self.SPACE_KEY = False, False, False

    def draw_text_game(self, text, size, x, y,fontColor=None,backgroundColor=None):
        font = pygame.font.Font(self.font_name,size)
        fontColor = fontColor or self.WHITE
        message = text
        snip = font.render("", True, fontColor)
        counter = 0
        speed = 30
        done = False    
        while counter < len(message) * speed:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            counter += 1

            snip = font.render(message[0:counter//speed], True, fontColor, backgroundColor)

            if backgroundColor:
                text_rect = snip.get_rect(topleft=(x, y))
                self.display.fill(backgroundColor, text_rect)

            self.window.blit(snip, (x, y))
            pygame.display.flip()
            
    def draw_fix_text(self, text, size, x, y,fontColor=None,backgroundColor=None):
        print("test")
        font = pygame.font.Font(self.font_name,size)
        fontColor = fontColor or self.WHITE
        text_surface = font.render(text, True, fontColor)
        original_text_rect = text_surface.get_rect()
        extended_text_rect = pygame.Rect(0, 0, original_text_rect.width + 10, original_text_rect.height + 6)
        extended_text_rect.center = (x, y)
        if backgroundColor:
            pygame.draw.rect(self.window, backgroundColor, extended_text_rect,0,7,7,7,7,7)
        text_surface_rect = text_surface.get_rect(center=extended_text_rect.center)
        self.window.blit(text_surface,text_surface_rect)

    def wait_for_space_bar(self):
        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    waiting = False
            self.timer.tick(30)  # Frame rate control to prevent high CPU usage