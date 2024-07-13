import pygame,sys
from button import Button

class Menu():
    def __init__(self, game):
        self.game = game
        self.mid_w, self.mid_h = self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2
        self.run_display = True
        self.cursor_rect = pygame.Rect(0, 0, 20, 20)
        self.offset = - 100
        self.BG = pygame.image.load("src/assets/mainMenuBG.jpg")
        self.itemSizeH1 = 70
        self.itemSizeH2 = 50
        self.size = 12
        self.font = pygame.font.Font(pygame.font.get_default_font(),self.size)

    def blit_screen(self):
        self.game.window.blit(self.BG, (0, 0))
        self.game.window.blit(self.game.display, (0, 0))
        pygame.display.update()
        self.game.reset_keys()

class MainMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = "Start"
        self.startx, self.starty = self.mid_w, self.mid_h - 40
        self.optionsx, self.optionsy = self.mid_w, self.mid_h + 25
        self.creditsx, self.creditsy = self.mid_w, self.mid_h + 90
        self.quitx, self.quity = self.mid_w, self.mid_h + 155
        self.cursor_rect.midtop = (self.startx + self.offset, self.starty)
        self.BG = pygame.image.load("src/assets/mainMenuBG.jpg")
        pygame.display.set_caption("Main Menu")

    def display_menu(self):
        self.run_display = True
        while self.run_display:

            self.blit_screen()

            MENU_MOUSE_POS = pygame.mouse.get_pos()
            self.game.check_events()
            self.check_input()


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
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                        pass
                    if OPTION_BUTTON.checkForInput(MENU_MOUSE_POS):
                        pass
                    if OPTION_BUTTON.checkForInput(MENU_MOUSE_POS):
                        pass
                    if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                        pygame.quit()
                        sys.exit()

    def move_cursor(self):
        if self.game.DOWN_KEY:
            if self.state == 'Start':
                self.cursor_rect.midtop = (self.optionsx + self.offset, self.optionsy)
                self.state = 'Options'
            elif self.state == 'Options':
                self.cursor_rect.midtop = (self.creditsx + self.offset, self.creditsy)
                self.state = 'Credits'
            elif self.state == 'Credits':
                self.cursor_rect.midtop = (self.startx + self.offset, self.starty)
                self.state = 'Start'
        elif self.game.UP_KEY:
            if self.state == 'Start':
                self.cursor_rect.midtop = (self.creditsx + self.offset, self.creditsy)
                self.state = 'Credits'
            elif self.state == 'Options':
                self.cursor_rect.midtop = (self.startx + self.offset, self.starty)
                self.state = 'Start'
            elif self.state == 'Credits':
                self.cursor_rect.midtop = (self.optionsx + self.offset, self.optionsy)
                self.state = 'Options'

    def check_input(self):
        self.move_cursor()
        if self.game.START_KEY:
            if self.state == 'Start':
                self.game.playing = True
            elif self.state == 'Options':
                self.game.curr_menu = self.game.options
            elif self.state == 'Credits':
                self.game.curr_menu = self.game.credits
            self.run_display = False

class OptionsMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = 'Volume'
        self.volx, self.voly = self.mid_w, self.mid_h + 20
        self.controlsx, self.controlsy = self.mid_w, self.mid_h + 40
        self.cursor_rect.midtop = (self.volx + self.offset, self.voly)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_input()
            self.game.display.fill((0, 0, 0))
            self.game.draw_text('Options', 20, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 30)
            self.game.draw_text("Volume", 15, self.volx, self.voly)
            self.game.draw_text("Controls", 15, self.controlsx, self.controlsy)
            self.draw_cursor()
            self.blit_screen()

    def check_input(self):
        if self.game.BACK_KEY:
            self.game.curr_menu = self.game.main_menu
            self.run_display = False
        elif self.game.UP_KEY or self.game.DOWN_KEY:
            if self.state == 'Volume':
                self.state = 'Controls'
                self.cursor_rect.midtop = (self.controlsx + self.offset, self.controlsy)
            elif self.state == 'Controls':
                self.state = 'Volume'
                self.cursor_rect.midtop = (self.volx + self.offset, self.voly)
        elif self.game.START_KEY:
            # TO-DO: Create a Volume Menu and a Controls Menu
            pass

class CreditsMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            if self.game.START_KEY or self.game.BACK_KEY:
                self.game.curr_menu = self.game.main_menu
                self.run_display = False
            self.game.display.fill(self.game.BLACK)
            self.game.draw_text('Credits', 20, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 20)
            self.game.draw_text('Made by me', 15, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 + 10)
            self.blit_screen()

