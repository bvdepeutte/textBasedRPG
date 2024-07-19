import pygame


class Button():
    def __init__(self, game, pos, text_input, size, font_color, base_color, hovering_color,font=None,):
        self.screen = game
        self.x_pos = pos[0]
        self.y_pos = pos[1]
        self.font = pygame.font.Font(font,size)
        self.font_color,self.base_color, self.hovering_color = font_color,base_color, hovering_color
        self.text_input = text_input
        self.text = self.font.render(self.text_input, True, font_color)
        self.size = size
        self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))
        self.rect = pygame.Rect(self.x_pos, self.y_pos, self.text_rect.width + 10, self.text_rect.height + 6)
        self.rect.center = (self.x_pos, self.y_pos)
        self.text_surface_rect = self.text.get_rect(center=self.rect.center)

        pygame.draw.rect(self.screen.display,base_color,self.rect,0,7,7,7,7,7)
    
    def checkForInput(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            return True
        return False

    def changeColor(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            self.text = self.font.render(self.text_input, True, self.hovering_color)
        else:
            self.text = self.font.render(self.text_input, True, self.font_color)
    
    def update(self):
        self.screen.display.blit(self.text, self.text_surface_rect)