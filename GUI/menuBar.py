import pygame as pg
#import tqdm

class menuBar: # Menu bar at the top of the screen
    def __init__(self, screen, x, y, width, height, color):
        self.screen = screen
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.items = []
        # In the menu bar we will have the following items:
             # Citizen count, city name, budget, satisfaction rate and time


    def draw(self):
        pg.draw.rect(self.screen, self.color, (self.x, self.y, self.width, self.height))

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
        self.font = pg.font.SysFont('Arial', 25)
        for item in self.items:
            screen.blit(self.font.render(item, True, (255, 255, 255)), (self.x, self.y))
            self.x += 100 # move the text to the right by 100 pixels
    
    """def progressBar(self, screen):
        for i in tqdm(range(1000)):
            pass """


# Path: GUI/menuBar.py

        
            