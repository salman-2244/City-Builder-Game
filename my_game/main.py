import pygame as pg
from Game import Game
import sys
sys.path.append('./GUIGame')
from Dropdown import Dropdown
def main():
    
    running = True # Setting a flag when the game is starte
    playing = True # Setting a flag when the player is playing

    pg.init()  # initializing pygame modules
    pg.display.set_caption("New York City") # setting title of the window
    screen = pg.display.set_mode((900, 600)) # creating and setting surface object
    clock = pg.time.Clock() # creating and setting time (for display on main Screen)
    

    game = Game(screen, clock)   # calling game class
    # world = World()
    # world.init_fields(screen)
    #world.draw_roads(screen)

    # while running: # as long as game is running 
        

    #     while playing: # as long as player is playing
           
            
    game.run() #running the game
            
    

    

if __name__ == "__main__":   # default : Checks if main is not imported 
    main()
    
        
    
    # adding the logic of the game to the screen        
    
    # pg.quit()
    # exit()