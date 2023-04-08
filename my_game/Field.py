# from Zones.zone import zone
import pygame as pg
class Field:
    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.size = size # size of the individual tile
        self.grid_pos = None
        self.color = (0, 255, 0, 0);
        self.zone = None # zone , when selcted change to the zone it is in
        self.road = False # bool to check if there is a road on the field, if true make the color grey over the background
        self.selected = False
        self.rect = pg.Rect(self.x, self.y, self.size, self.size)
        
    def set_zone(self, zone):
        self.zone = zone
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        