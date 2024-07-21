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
        self.font_path = 'src/assets/hood_brothers.ttf'
        self.BLACK, self.WHITE, self.RED, self.GREY = (0, 0, 0), (255, 255, 255), (122, 38, 58), (128, 128, 128)
        self.text_size = 35
        self.title = 90
        self.subtitle = 60
        self.timer = pygame.time.Clock()
        self.UI_REFRESH_RATE = self.timer.tick(30)
        self.playing = True
        self.SPACE_KEY, self.UP_KEY, self.DOWN_KEY = False, False, False
        self.title_BG = pygame.image.load('src/assets/new_game_title_screen.jpg')
        self.manager = pygame_gui.UIManager((display_w, display_h))



    def blit_screen(self):
        self.window.blit(self.display, (0, 0))
        pygame.display.update()

    def game_loop(self):
        fontAvalaible = pygame.font.get_fonts()
        print(fontAvalaible)
        while self.playing:
            self.display.fill(self.BLACK)
            self.blit_screen()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.window.blit(self.title_BG,(0,0))
            
            # Title screen
            pygame.display.update()
            time.sleep(0.5)
            self.draw_fix_text("The Project:", self.title, self.DISPLAY_W/2, self.DISPLAY_H/4, self.WHITE, self.RED)
            pygame.display.update()
            time.sleep(0.5)
            self.draw_fix_text("A text based RPG",self.subtitle, self.DISPLAY_W/2, self.DISPLAY_H* 8/20, self.WHITE)
            pygame.display.update()
            time.sleep(0.5)
            self.draw_fix_text("Created by: Vandepeutte Bastien",self.text_size, self.DISPLAY_W/2, self.DISPLAY_H*6/10, self.WHITE)
            pygame.display.update()
            time.sleep(0.5)
            self.draw_fix_text("Press space to continue",self.text_size,self.DISPLAY_W /2, self.DISPLAY_H - 60,None,self.BLACK)
            self.wait_for_space_bar()
            pygame.display.update()
            
            
            # Introduction
            self.display.fill(self.BLACK)
            self.window.blit(self.title_BG,(0,0))

            self.draw_text_game('During the last decades, the galaxy is at war with an unknown threat...',self.text_size,self.DISPLAY_W /12, self.DISPLAY_H * 1/8,None,self.GREY)
            self.draw_text_game("The Earth-Mars Alliance has been created to survive the conflict.",self.text_size,self.DISPLAY_W /12, self.DISPLAY_H * 1/8+35,None,self.GREY)
            self.draw_text_game("But they still don't know who they are fighting",self.text_size,self.DISPLAY_W /12, self.DISPLAY_H * 1/8+70,None,self.GREY)
            self.draw_text_game('Untill recently... the navy has collected a crucial information.',self.text_size,self.DISPLAY_W /12, self.DISPLAY_H * 1/8+105,None,self.GREY)
            self.draw_text_game('The ennemy main flotilla is docked around a planet',self.text_size,self.DISPLAY_W /12, self.DISPLAY_H * 1/8+140,None,self.GREY)
            self.draw_text_game('They even received information around a security breach, we could exploit',self.text_size,self.DISPLAY_W /12, self.DISPLAY_H * 1/8+175,None,self.GREY)
            self.draw_text_game('But nothing worked as planned...',self.text_size,self.DISPLAY_W /12, self.DISPLAY_H * 1/8+210,None,self.GREY)
            time.sleep(0.5)
            self.draw_text_game("It wasn't the main flottilla that was stationed there. But they were deployed nearby",self.text_size,self.DISPLAY_W /12, self.DISPLAY_H * 1/8+245,None,self.GREY)
            self.draw_text_game("Even if the first part of the battle was in favour of our troops",self.text_size,self.DISPLAY_W /12, self.DISPLAY_H * 1/8+280,None,self.GREY)
            self.draw_text_game("The intervention of the ennemy main flotilla turned the tide...",self.text_size,self.DISPLAY_W /12, self.DISPLAY_H * 1/8+315,None,self.GREY)
            self.draw_text_game("You were included in the middle of this shitstorm, you've suffer and lost",self.text_size,self.DISPLAY_W /12, self.DISPLAY_H * 1/8+350,None,self.GREY)
            self.draw_text_game("Despite the turnmoil, your luck striked and you were able to reach a ship leaving the sector",self.text_size,self.DISPLAY_W /12, self.DISPLAY_H * 1/8+385,None,self.GREY)
            self.draw_fix_text("Press space to continue",self.text_size,self.DISPLAY_W /2, self.DISPLAY_H - 60,None,self.BLACK)
            self.wait_for_space_bar()

            # User Creation
            self.display.fill(self.BLACK)
            self.window.blit(self.title_BG,(0,0))

            playercharacter = characterCreation(self)
            playercharacter.selectLiveForm()
            #playercharacter.selectClass()
            #print("After some rest, you need a moment to come up with a plan based on your strengths and weaknesses")
            #playercharacter.selectTraits()
            self.draw_fix_text("Press space to continue",self.text_size,self.DISPLAY_W /2, self.DISPLAY_H - 60,None,self.BLACK)
            self.wait_for_space_bar()

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
        font = pygame.font.Font(self.font_path,size)
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
        font = pygame.font.Font(self.font_path,size)
        fontColor = fontColor or self.WHITE
        text_surface = font.render(text, True, fontColor)
        original_text_rect = text_surface.get_rect()
        extended_text_rect = pygame.Rect(0, 0, original_text_rect.width + 10, original_text_rect.height + 6)
        extended_text_rect.center = (x, y)
        if backgroundColor:
            pygame.draw.rect(self.window, backgroundColor, extended_text_rect,0,7,7,7,7,7)
        text_surface_rect = text_surface.get_rect(center=extended_text_rect.center)
        self.window.blit(text_surface,text_surface_rect)
        pygame.display.flip()

    def wait_for_space_bar(self):
        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    waiting = False
            self.UI_REFRESH_RATE  # Frame rate control to prevent high CPU usage
    
    def input_box(self, x, y, sizeX, sizeY, object_id):

        text_input = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((x, y), (sizeX, sizeY)), manager=self.manager,
                                               object_id = object_id)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if (event.type == pygame_gui.UI_TEXT_ENTRY_FINISHED and
                    event.ui_object_id == object_id):
                    return event.text

                self.manager.process_events(event)
            
            self.manager.update(self.UI_REFRESH_RATE/1000)

            self.manager.draw_ui(self.window)

            pygame.display.update()
        

