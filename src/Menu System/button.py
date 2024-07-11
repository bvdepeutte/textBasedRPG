import pygame


class Button():
    def __init__(self, game, pos, text_input, size, font, font_color, base_color, hovering_color):
        self.game = game
        self.x_pos = pos[0]
        self.y_pos = pos[1]
        self.font = font
        self.font_color = font_color
        self.base_color, self.hovering_color = base_color, hovering_color
        self.text_input = text_input
        self.size = size
        self.rect = self.game.draw_text(self.text_input, self.size, self.x_pos, self.y_pos, self.font_color,self.base_color)
    
    def checkForInput(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            return True
        return False

    def changeColor(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            self.text = self.font.render(self.text_input, True, self.hovering_color)
        else:
            self.text = self.font.render(self.text_input, True, self.base_color)