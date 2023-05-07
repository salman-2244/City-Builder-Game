# from Zones.zone import zone
import pygame as pg
class Field:
    def __init__(self, x, y, size):
        self.x = x # in 2d array
        self.y = y
        self.size = size # size of the individual tile
        self.grid_pos = None
        self.color = (86, 148, 70,0);
        self.building = "";
        self.zone = None # zone , when selcted change to the zone it is in
        self.road = False  # bool to check if there is a road on the field, if true make the color grey over the background
        self.selected = False # Holds if the field is selected or not
        self.rect = pg.Rect(self.x, self.y, self.size, self.size)  # drawing rect on grid
        self.id = None
        
    def getX(self):
        return self.x

    def connectsTo(self):
        if self.road == True:
            reachables = [(self.x, self.y+55), (self.x, self.y-55), (self.x+55, self.y), (self.x-55, self.y)]
            return reachables
    
    def set_zone(self, zone):
        self.zone = zone
    def set_road(self):
        self.road = True
    def build_road(self):
        if self.road == True:
            self.color  = (128, 128, 128)
    
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        