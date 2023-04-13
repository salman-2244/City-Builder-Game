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
        #screen = Game.screen # setting screen object to screen
        #clock = Game.clock    # setting clock object
        field_size = 30  # size of each field
        grid_rows = int(screen.get_height() / field_size)  # calculate rows (use later)
        grid_cols = int(screen.get_width() / field_size)  # calculate cols
        pos = (0, 90)
        """for row in range(grid_cols):
            for col in range(grid_rows):
                if(row == 3):
                    self.Fields[row][col] = Field(row * field_size, col * field_size, field_size, pos)
        print(self.Fields[0][0])"""
        self.Fields = [[ Field(x, y, field_size) for x in range(grid_rows)] for y in range (grid_cols)]
        
        # addition of the color in the 2d list for the road in the 3rd row
        print(self.Fields)
        """for field in self.Fields:
                for f in field:
                    print(f)
        if(f.getX() == 3): # if the field is in the 3rd row
        f.set_zone("General") # set the zone to general
                        f.set_road() # set the road to true
                        f.build_road() # build the road
"""
                


            
    def get_field(self, x, y):
        for field in self.Fields:
            if field.x == x and field.y == y:
                return field
        return None
    
    """def draw_roads(self, surf): # drawing roads
        for field in self.Fields:
            if field.road:
                pg.draw.rect(surf, field.color, pg.Rect(field.posX, field.posY, 30, 30))
                """

    def add_road(self, x, y): # adding roads to the field
        field = self.get_field(x, y)
        if field is not None:
            field.road = True
    
    def check_road(self, x, y): # checking if there is a road on the field
        field = self.get_field(x, y)
        if field is not None:
            return field.road
        return False 

    def get_fields(self): # getting the fields
        return self.Fields
    
    def add_zone(self, zone):
        self.Zones.append(zone)
    
    def set_zone(self, x, y, zone):
        field = self.get_field(x, y)
        if field is not None:
            field.set_zone(zone)
    
    def get_zone(self, x, y):
        field = self.get_field(x, y)
        if field is not None:
            return field.zone
        return None
    
    def get_zones(self):
        return self.Zones
    
    
    
        
    