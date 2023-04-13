# from Zones.zone import zone
import pygame as pg
class Field:
<<<<<<< HEAD
    def __init__(self, x, y, size, ):  # (pos) removed one un-necessery parameter 
        self.x = x 
=======
    def __init__(self, x, y, size):
        self.x = x # in 2d array
>>>>>>> Changes
        self.y = y
        self.size = size # size of the individual tile
        self.grid_pos = None
        self.color = (0, 255, 0, 0);
<<<<<<< HEAD
        self.zone = None  # zone , when selcted change to the zone it is in
=======
        self.zone = None # zone , when selcted change to the zone it is in
>>>>>>> Changes
        self.road = False  # bool to check if there is a road on the field, if true make the color grey over the background
        self.selected = False # Holds if the field is selected or not
        self.rect = pg.Rect(self.x, self.y, self.size, self.size)  # drawing rect on grid
        # self.posX = pos[0] # position on the grid
        # self.posY = pos[1]
        
    def getX(self):
        return self.x
    
    def set_zone(self, zone):
        self.zone = zone
    def set_road(self):
        self.road = True
    def build_road(self):
        if self.road == True:
            self.color  = (128, 128, 128)
    
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        