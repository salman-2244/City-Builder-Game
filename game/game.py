import pygame as pg # importing pygame as pg
import sys  # importing sys library

class Game:  # initiating game class.
    
    def __init__(self, screen, clock):
         self.screen = screen  # setting screen object to screen
         self.clock = clock    # setting clock object
         
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
                     
    def update(self):
        pass;
                    
    def draw(self):
        self.screen.fill((0, 255, 0)) # fill the screen 
        pg.display.flip();  # update the changes in display
        
        
        