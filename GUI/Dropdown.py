import pygame as pg
import sys
from GUI.button import Button
class Dropdown():
    def __init__(self,text,x,y,w,h, main, options, image): # add button image here
        self.__x = x
        self.__y = y
        self.__w = w
        self.__h = h
        self.__text = text
        self.__rect = pg.Rect(x,y,w,h)
        self.__main = main
        self.__drawMenu = False
        self.__menuActive = False
        self.options = options
        self.__activeOption = -1
        self.ins = image
        self.ins_button = Button(self.__x, self.__y, self.ins, 1)
        # each option is a button

    
    def draw(self, surface):
        self.ins_button.update(surface)
       
        # if draw menu is clicked 
        if self.__drawMenu:
            for i, text in enumerate(self.options):
                rect = self.ins_button.getRect().copy()
                print(rect.y)
                rect = rect.move(0, (i+ 1) * rect.height)
                pg.draw.rect(surface, (255, 255, 255), rect, 0)
                msg = self.__text.render(text,1, (0, 0, 0))
                surface.blit(msg, msg.get_rect(center = rect.center)) # maybe change this part

    def update(self, events):
        clickCount = 0
        mouse = pg.mouse.get_pos()
        self.__menuActive = self.ins_button.checkInput(mouse)
        self.__activeOption = -1

        if self.__menuActive:
            clickCount += 1
        # checking from the options
        for i in range(len(self.options)):
            rect = self.ins_button.getRect().copy()
            rect = rect.move(0, (i+ 1) * rect.height)
            # have a rect of the button and then check if the mouse is in the rect
            if rect.collidepoint(mouse):
                self.__activeOption = i

                clickCount += 1
        
        for event in events:
            if event.type == pg.MOUSEBUTTONDOWN:
                if self.__menuActive:
                    self.__drawMenu = not self.__drawMenu
                elif self.__activeOption > -1 and self.__drawMenu: 
                    self.__drawMenu = False
                    return self.__activeOption
        return -1
    
pg.init()
clock = pg.time.Clock()
screen = pg.display.set_mode((800, 600))

image = pg.image.load("Buttons/ini.png")

l1 = list1 = Dropdown(pg.font.SysFont(None, 30), 
    50, 50, 200, 50,  
    "Zones", ["General", "Residential", "Commercial", "Industrial"], image)



run = True
while run:
    clock.tick(100)

    event_list = pg.event.get()
    for event in event_list:
        if event.type == pg.QUIT:
            run = False

    selected_option = list1.update(event_list)
    if selected_option >= 0:
        list1.__main = list1.options[selected_option]
        print("Selected option: ", list1.options[selected_option])

    screen.fill((255, 255, 255))
    list1.draw(screen)
    pg.display.flip()
    
pg.quit()
exit()

            


