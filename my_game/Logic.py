import pygame as pg 
import sys  # importing sys library
from my_game.game import Game
from my_game.Field import Field

class World:
    def __init__(self):
        self.Fields = []
        self.Zones = []
        self.Roads = []
        self.Name = "New York City"
        self.Bank = 0
        self.Citizens = []
        self.citizen_tax = 18
        self.citizen_happiness = 0


    def init_fields(self, screen): # initializing fields
        #initialize 2D array which represents the grid
        screen = Game.screen # setting screen object to screen
        clock = Game.clock    # setting clock object
        field_size = 30  # size of each field
        grid_rows = int(screen.get_height() / field_size)  # calculate rows (use later)
        grid_cols = int(screen.get_width() / field_size)  # calculate cols
        for row in range(grid_rows):
            for col in range(grid_cols):
                self.Fields.append(Field(col * field_size, row * field_size, field_size))
        
    def get_field(self, x, y):
        for field in self.Fields:
            if field.x == x and field.y == y:
                return field
        return None
    
               