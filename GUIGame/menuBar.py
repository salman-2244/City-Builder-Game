import pygame as pg
from ProgressBar import TextProgress
#import tqdm

class menuBar: # Menu bar at the top of the screen
    def __init__(self, screen, x, y, width, height, color, items):
        self.screen = screen
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.items = []
        # In the menu bar we will have the following items:
             # Citizen count, city name, budget, satisfaction rate and time


    def draw(self, content):
        pg.draw.rect(self.screen, self.color, (self.x, self.y, self.width, self.height))
        # how to dispaly content in the rect
        
    def update(self):
        self.draw()

    def checkInput(self, mouse_pos):
        if self.x <= mouse_pos[0] <= self.x + self.width and self.y <= mouse_pos[1] <= self.y + self.height:
            return True
        else:
            return False
        
    def addItem(self, item):
        self.items.append(item)
    
    def displayItems(self, screen):
        self.font = pg.font.SysFont('Arial', 13)
        for item in self.items:
            screen.blit(self.font.render(item, True, (255, 255, 255)), (self.x, self.y))
            self.x += 100 # move the text to the right by 100 pixels
            pg.display.update()
    
    def createProgressBar(self, screen, x, y, width, height, color, value):
        bigfont = pg.font.Font(None, 13)
        white = 255, 255, 255
        renderer = TextProgress(bigfont, "Satisfaction", white, (40, 40, 40))
        text = renderer.render(screen, value)
    
    
    
    def updateItems(self, screen, items):
        self.items = items
        self.displayItems(screen)
        

    

# Path: GUI/menuBar.py

        
            