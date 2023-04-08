import pygame as pg
from GUI.Dropdown import Dropdown
# need to change if put game in other folder.

from game import Game # need to change if put game in other folder.
# from game import Field 
from my_game.Logic import World
def main():
    
    running = True # Setting a flag when the game is started
    playing = True # Setting a flag when the player is playing

    pg.init()  # initializing pygame modules
    pg.display.set_caption("New York City") # setting title of the window
    screen = pg.display.set_mode((900, 600)) # creating and setting surface object
    clock = pg.time.Clock() # creating and setting time (for display on main Screen)
    

    game = Game(screen, clock)   # calling game class

    while running: # as long as game is running 

        while playing: # as long as player is playing
           
            game.run() #running the game
    
    image = pg.image.load("Buttons/ini.png")
    
    l1 = list1 = Dropdown(pg.font.SysFont(None, 30), 
    50, 50, 200, 50,  
    "Zones", ["General", "Residential", "Commercial", "Industrial"], image)

    # adding the logic of the game to the screen        
    world = World()
    World.init_fields(Game.screen)

if __name__ == "__main__":   # default : Checks if main is not imported 
    main()