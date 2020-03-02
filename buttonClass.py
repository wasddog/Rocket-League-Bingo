import pygame
from settings import *


class Button:
    def __init__(self, x, y, width, height,text=None , colour=(73,73,73), highlightColour=(189,189,189)):
        self.image = pygame.Surface((width,height))
        self.pos = (x,y)
        self.rect = self.image.get_rect()
        self.width = width
        self.height = height
        self.mousePos = None
        self.text = text
        self.colour = colour
        self.font = pygame.font.SysFont("Comic Sans MS", 20)
        self.highlightColour = highlightColour
        self.highlighted = False

    def update(self, mouse):
        if self.rect.collidepoint(mouse):
            self.highlighted = True
        else:
            self.highlighted = False

    def draw(self,window):
        self.image.fill(self.highlightColour if self.highlighted else self.colour)
        self.drawText(self.image)
        window.blit(self.image, self.pos)


    def drawText(self, window):
        self.textToScreen(window, "Generate new bingo!", [5,3])

    def textToScreen(self, window, text, pos):
        font = self.font.render(text, True, WHITE)
        window.blit(font, pos)
