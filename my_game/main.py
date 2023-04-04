import pygame as pg
from my_game import game # need to change if put game in other folder.

def main():
    
    running = True # Setting a flag when the game is started
    playing = True # Setting a flag when the player is playing

    pg.init()  # initializing pygame modules
    pg.display.set_caption("New York City") # setting title of the window
    screen = pg.display.set_mode((900, 600)) # creating and setting surface object
    clock = pg.time.Clock() # creating and setting time (for display on main Screen)
    

    game = game(screen, clock)   # calling game class

    while running: # as long as game is running 

        while playing: # as long as player is playing
           
            game.run() #running the game

if __name__ == "__main__":   # default : Checks if main is not imported 
    main()