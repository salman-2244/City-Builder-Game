import pygame as pg
import sys
sys.path.append('./GUIGame')
from button import Button
class Dropdown():
    def __init__(self,text,x,y,w,h, main, options, image): # add button image here
        """_summary_

        Args:
            text (String): text to be displayed
            x (Integer): x coordinate
            y (Integer): y coordinate
            w (Integer): width
            h (Integer): height
            main (screen): screen to draw on
            options (list): list of options
            image (String): path to image
        """
        pg.sprite.Sprite.__init__(self)
        self.__x = x
        self.__y = y
        self.__w = w
        self.__h = h
        self.__drawMenu = False
        self.__menuActive = False
        self.options = options
        self.__activeOption = -1
        self.ins = image
        self.ins_button = Button(self.__x, self.__y, self.ins, 1)
        self.killMe = False
        self.clickCount = 0
        # each option is a button

    
    def drawDD(self, surface):
        """_summary_

        Args:
            surface (screen): screen to draw on
            Draw the dropdown menu
        """
        self.ins_button.update(surface)
        self.killMe = False
        # if draw menu is clicked 
        if self.__drawMenu:
            for i, text in enumerate(self.options):
                rect = self.ins_button.getRect().copy()
                # rect = rect.move(0, (i+ 1) * rect.height/2)
                # #pg.draw.rect(surface, (0, 0, 0), rect, 0)
                # msg = self.__text.render(text,1, (0, 0, 0))
                self.options[i].rect = rect
                self.options[i].rect = rect.move(0, (i+ 1) * rect.height)
                self.options[i].update(surface)
                #surface.blit(self.options[i].rect, self.options[i].rect(center = rect.center))

    def update(self): # trying to kill the sprite of drawing the buttons
        """
        Update the dropdown menu sprirte
        """
        if self.clickCount > 0:
            self.kill()
        
        
    def updateDD(self, events):
        """_summary_

        Args:
            events (event list): list of events
        listen for events and update the dropdown menu

        Returns:
            Integer: index of option chosen
        """
        for i in range(len(self.options)):
            rect = self.ins_button.getRect().copy()
            self.options[i].rect = rect
            self.options[i].rect = rect.move(0, (i+ 1) * rect.height)

        for event in events:
            if event.type == pg.MOUSEBUTTONDOWN:
                mouse = pg.mouse.get_pos()
                self.__menuActive = self.ins_button.checkInput(mouse)
                self.__activeOption = -1
                
            if self.__menuActive:
                print("Menu activated\n")
                self.clickCount += 1

            for i in range(len(self.options)):
                if self.options[i].isClicked(events):
                    self.__activeOption = i
                    self.__menuActive = True
                    print(self.__activeOption)
                    print("jjk")
                    self.clickCount += 1
                    print("Option chosen: %d",self.__activeOption)
                    self.killMe = True
                    return self.__activeOption
                    
            if not self.__menuActive and self.__activeOption == -1:
                self.__drawMenu = False
                
            if self.__menuActive:
                self.__drawMenu = not self.__drawMenu
            elif self.__activeOption >= 0 and self.__drawMenu: 
                self.__drawMenu = False
                return self.__activeOption
        return -1
