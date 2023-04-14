import pygame as pg 
import sys  # importing sys library
from my_game.game import Game
from my_game.Field import Field
from Zones.zone import zone

class World:
    def __init__(self):
        self.Fields = []
        self.Zones = []
        self.Roads = []
        self.Name = "New York City"
        self.Bank = 200000 # initial budget of the city
        self.Citizens = 0
        self.citizen_tax = 18 # in percentage
        self.citizen_happiness = 0 # in pertentage


    def init_fields(self, screen): # initializing fields
        field_size = 30  # size of each field
        grid_rows = int(screen.get_height() / field_size)  # calculate rows (use later)
        grid_cols = int(screen.get_width() / field_size)  # calculate cols
        pos = (0, 90)
        self.Fields = [[ Field(x, y, field_size) for x in range(grid_rows)] for y in range (grid_cols)]


    def get_field(self, x, y):
        for field in self.Fields:
            if field.x == x and field.y == y:
                return field
        return None
    

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
    
    def addUpCitizen(self): # number of citizens
        for i in range(self.Zones): 
            self.Citizens += i.getResidents()
    def get_citizens(self):
        return self.Citizens
    
    



        
    