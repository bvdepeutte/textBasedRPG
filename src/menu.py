import pygame,sys
from button import Button

class Menu():
    def __init__(self, game):
        self.game = game
        self.mid_w, self.mid_h = self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2
        self.run_display = True
        self.cursor_rect = pygame.Rect(0, 0, 20, 20)
        self.offset = - 100
        self.BG = None
        self.itemSizeH1 = 70
        self.itemSizeH2 = 50
        self.size = 12
        self.font = pygame.font.Font(pygame.font.get_default_font(),self.size)
        pygame.display.set_caption("Text RPG")


    def blit_screen(self):
        self.game.window.blit(self.BG, (0, 0))
        self.game.window.blit(self.game.display, (0, 0))
        pygame.display.update()
        self.game.reset_keys()

class MainMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = "New Game"
        self.startx, self.starty = self.mid_w, self.mid_h - 40
        self.optionsx, self.optionsy = self.mid_w, self.mid_h + 25
        self.creditsx, self.creditsy = self.mid_w, self.mid_h + 90
        self.quitx, self.quity = self.mid_w, self.mid_h + 155
        self.cursor_rect.midtop = (self.startx + self.offset, self.starty)
        self.BG = pygame.image.load("src/assets/mainMenuBG.jpg")

    def display_menu(self):
        while self.run_display:

            self.blit_screen()

            MENU_MOUSE_POS = pygame.mouse.get_pos()
            self.game.check_events()


            self.game.display.blit(self.BG,(0,0))
            
            self.game.draw_text('Main Menu', self.itemSizeH1,self.mid_w, self.mid_h/2, self.game.WHITE,self.game.RED)
            PLAY_BUTTON = Button(self.game,(self.startx,self.starty),"New Game",self.itemSizeH2,self.game.WHITE,self.game.RED,self.game.BLACK)
            PLAY_BUTTON.update()
            OPTION_BUTTON = Button(self.game,(self.optionsx,self.optionsy),"Settings",self.itemSizeH2,self.game.WHITE,self.game.RED,self.game.BLACK)
            OPTION_BUTTON.update()
            CREDIT_BUTTON = Button(self.game,(self.creditsx,self.creditsy),"Credit",self.itemSizeH2,self.game.WHITE,self.game.RED,self.game.BLACK)
            CREDIT_BUTTON.update()
            QUIT_BUTTON = Button(self.game,(self.quitx,self.quity),"Quit",self.itemSizeH2,self.game.WHITE,self.game.RED,self.game.BLACK)
            QUIT_BUTTON.update()

            for button in [PLAY_BUTTON, OPTION_BUTTON, CREDIT_BUTTON, QUIT_BUTTON]:
                button.changeColor(MENU_MOUSE_POS)
                button.update()
                if button.checkForInput(MENU_MOUSE_POS) and button == PLAY_BUTTON:
                    self.state = "New Game"
                elif button.checkForInput(MENU_MOUSE_POS) and button == OPTION_BUTTON:
                    self.state = "Option"
                elif button.checkForInput(MENU_MOUSE_POS) and button == CREDIT_BUTTON:
                    self.state = "Credit"
                elif button.checkForInput(MENU_MOUSE_POS) and button == QUIT_BUTTON:
                    self.state = "Quit" 

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                        self.game.start_game = True
                    if OPTION_BUTTON.checkForInput(MENU_MOUSE_POS):
                        pass
                    if CREDIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                        self.game.curr_menu = self.game.credits
                        self.game.curr_menu.display_menu()
                    if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                        pygame.quit()
                        sys.exit()


class OptionsMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        
    def display_menu(self):
        pass

    def check_input(self):
        pass

class CreditsMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.BG = pygame.image.load("src/assets/creditMenuBG.jpg")

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            if self.game.START_KEY or self.game.BACK_KEY:
                self.game.curr_menu = self.game.main_menu
                self.run_display = False
            self.game.display.blit(self.BG,(0,0))
            self.game.draw_text('Credits', 20, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 20)
            self.game.draw_text('Made by Bastien Vandepeutte for personnal project', 15, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 + 10)
            self.blit_screen()

