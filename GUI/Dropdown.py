import pygame as pg
import sys

class Dropdown():
    def __init__(self,x,y,w,h, main, options):
        self.__x = x
        self.__y = y
        self.__w = w
        self.__h = h
        self.__rect = pg.Rect(x,y,w,h)
        self.__main = main
        self.__drawMenu = False
        self.__menuActive = False
        self.__options = options
        self.__activeOption = -1

    def draw(self, surface):
        pg.draw.rect(surface, (0,0,0), self.__rect)
        msg = self.font.render(self.main, 1, (0, 0, 0))
        surface.blit(msg, msg.get_rect(center = self.rect.center))
        # if draw menu is clicked 
        if self.__drawMenu:
            for i, text in enumerate(self.options):
                rect = self.rect.copy()
                rect.y += (i+1) * self.rect.height
                msg = self.font.render(text, 1, (0, 0, 0))
                surface.blit(msg, msg.get_rect(center = (self.rect.centerx, self.rect.centery + 20 * (i + 1)))) # maybe change this part

    def update(self, events):
        mouse = pg.mouse.get_pos()
        self.__menuActive = self.rect.collidepoint(mouse)
        

            


