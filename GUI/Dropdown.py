import pygame as pg
import sys
from GUI.button import Button
class Dropdown():
    def __init__(self,text,x,y,w,h, main, options):
        self.__x = x
        self.__y = y
        self.__w = w
        self.__h = h
        self.__text = text
        self.__rect = pg.Rect(x,y,w,h)
        self.__main = main
        self.__drawMenu = False
        self.__menuActive = False
        self.__options = options
        self.__activeOption = -1
         

    
    def draw(self, surface):
        pg.draw.rect(surface, (0,0,0), self.__rect)
        msg = self.__text.render(self.__main, 1, (0, 0, 0))
        surface.blit(msg, msg.get_rect(center = self.__rect.center))instructions = 

        # create the button for the dropdown
        ins = pg.image.load("Buttons/ini.png")
        # button instances
        ins_button = Button(self.__x, self.__y, ins, 1)
        # if draw menu is clicked 
        if self.__drawMenu:
            for i, text in enumerate(self.__options):
                rect = self.__rect.copy()
                rect.y += (i+1) * self.__rect.height
                msg = self.__text.render(text,1, (0, 0, 0))
                surface.blit(msg, msg.get_rect(center = rect.center)) # maybe change this part

    def update(self, events):
        mouse = pg.mouse.get_pos()
        self.__menuActive = self.__rect.collidpoint(mouse)
        self.__activeOption = -1

        # checking from the options
        for i in range(len(self.__options)):
            rect = self.__rect.copy()
            rect.y += (i+1) * self.__rect.height
            if rect.collidepoint(mouse):
                self.__activeOption = i
                break
        if not self.__menuActive:
            self.__drawMenu = False
        
        for event in events:
            if event.type ++ pg.MOUSEBUTTONDOWN:
                if self.__menuActive:
                    self.__drawMenu = not self.__drawMenu
                elif self.__activeOption > -1 and self.__drawMenu: 
                    self.__drawMenu = False
                    return self.__activeOption
        return -1
    
pg.init()
clock = pg.time.Clock()
screen = pg.display.set_mode((800, 600))
COLOR_INACTIVE = (100, 80, 255)
COLOR_ACTIVE = (100, 200, 255)
COLOR_LIST_INACTIVE = (255, 100, 100)
COLOR_LIST_ACTIVE = (255, 150, 150)


l1 = list1 = Dropdown(pg.font.SysFont(None, 30), 
    50, 50, 200, 50,  
    "Zones", ["General", "Residential", "Commercial", "Industrial"])



run = True
while run:
    clock.tick(100)

    event_list = pg.event.get()
    for event in event_list:
        if event.type == pg.QUIT:
            run = False

    selected_option = list1.update(event_list)
    if selected_option >= 0:
        list1.__main = list1.__options[selected_option]
        print("Selected option: ", list1.options[selected_option])

    screen.fill((255, 255, 255))
    list1.draw(screen)
    pg.display.flip()
    
pg.quit()
exit()

            


