import pygame as pg # importing pygame as pg
from Field import Field


import sys  # importing sys library
from pygame.locals import * # So I can use the draw module.

class Game:  # initiating game class.
    
    def __init__(self, screen, clock):
         self.screen = screen  # setting screen object to screen
         self.clock = clock    # setting clock object
         self.field_size = 30  # size of each field
         self.grid_rows = int(screen.get_height() / self.field_size)  # calculate rows (use later)
         self.grid_cols = int(screen.get_width() / self.field_size)  # calculate cols
         self.line_width = 1   # width of grid lines
         self.fields = []

         
         
    def run(self): 
        self.playing = True 
        self.timer = 0 
        while self.playing: # while player is playing
            self.clock.tick(60) # limiting the game loop to a maximum of 60 frames per second
            self.events() 
            self.update()
            self.draw()
            
            
    def events(self):
        for event in pg.event.get(): # getting all events
            if event.type == pg.QUIT: # if player click exit then exit
                pg.quit();
                sys.exit()
            elif event.type == pg.KEYDOWN:  # if key is pressed
                if event.key == pg.K_ESCAPE: # if player press esc key then exit
                     pg.quit();
                     sys.exit();
            elif event.type == pg.MOUSEBUTTONUP:
                pos = pg.mouse.get_pos()
                print(pos);
                     
    def update(self):
        pass;

    # addition of the bacground image         
    def addBackground(self):
        bg = pg.image.load("assets/bg.jpeg")
        self.screen.blit(bg, (0, 0))
        
    


    def drawGrid(self):
        self.addBackground()
        for x in range(0, self.screen.get_width(), self.field_size): # drawing vertical lines
           pg.draw.line(self.screen, (255, 255, 255), (x, 0), (x, self.screen.get_height()), self.line_width)
        for y in range(0, self.screen.get_height(), self.field_size): # drawing horizonal lines
           pg.draw.line(self.screen, (255, 255, 255), (0, y), (self.screen.get_width(), y), self.line_width) 
           
       
        # for row in range(self.grid_rows):
        #     for col in range(self.grid_cols):
        #         x = col * self.field_size
        #         y = row * self.field_size
        #         field = Field(x, y, self.field_size, None)
        #         self.fields.append(field)
                         
                    
    def draw(self):
        self.screen.fill((0, 255, 0)) # fill the screen 
        self.drawGrid() # drawing the grid
        pg.display.flip();  # update the changes in display
        
        
    
        
    
    

        
        