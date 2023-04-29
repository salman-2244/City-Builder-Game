import pygame as pg
from ProgressBar import TextProgress
import sys
import datetime
#import tqdm

class menuBar: # Menu bar at the top of the screen
    def __init__(self, screen, x, y, width, height, items):
        self.screen = screen
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.items = items
        # In the menu bar we will have the following items:
             # Citizen count, city name, budget, satisfaction rate and time

        
    def update(self, screen, items):
        self.items = items
        self.displayItems(screen)
        

    def checkInput(self, mouse_pos):
        if self.x <= mouse_pos[0] <= self.x + self.width and self.y <= mouse_pos[1] <= self.y + self.height:
            return True
        else:
            return False
        
    def addItem(self, item):
        self.items.append(item)
    
    
    def displayItems(self, screen, items, value):
        self.font = pg.font.SysFont('Arial', 25)
        for item in items:
            s = str(item)
            screen.blit(self.font.render(s, True, (255, 255, 255)), (self.x, self.y))
            self.x += 200 # move the text to the right by 100 pixels
                # self.createProgressBar(screen, i)
            pg.time.delay(10)
            pg.display.update()
            # self.createProgressBar(screen, value)
    
    def createProgressBar(self, screen, value):
        bigfont = pg.font.Font(None, 13)
        white = 255, 255, 255
        renderer = TextProgress(bigfont, "Satisfaction", white, (40, 40, 40))
        text = renderer.render(screen, value)

    

    

# Path: GUI/menuBar.py

        
            