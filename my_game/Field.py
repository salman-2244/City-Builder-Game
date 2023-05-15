# from Zones.zone import zone
import pygame as pg
class Field:
    def __init__(self, x, y, size):
        self.x = x # in 2d array
        self.y = y
        self.size = size # size of the individual tile
        self.grid_pos = None
        self.color = (86, 148, 70);
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
    
    def destructible(self, fields):
        cond1 = True; cond2 = True; cond3 = True; cond4 = True;
        unzoned = True
         
        if self.road == True and self.zone.typ == "general":
            for field in fields:
                if( self.y + 50 ==  field.y and field.x == self.x and field.road == True):
                    cond1 = False
                if(self.y + 50 ==  field.y and field.x == self.x and field.zone.typ != "general"):
                    unzoned = False
                if (self.y - 50 ==  field.y and field.x == self.x and field.road == True):
                    cond2 = False
                if( self.y - 50 ==  field.y and field.x == self.x and field.zone.typ != "general"):
                    unzoned = False
                if (self.x + 50 ==  field.x and field.y == self.y and field.road == True):
                    cond3 = False
                if( self.x + 50 ==  field.x and field.y == self.y and field.zone.typ != "general"):
                    unzoned = False
                
                if (self.x -50 ==  field.x and field.y == self.y and field.road == True):
                    cond4 = False
                if( self.x - 50 ==  field.x and field.y == self.y and field.zone.typ != "general"):
                    unzoned = False
            if unzoned == False:
                return False
            if cond1 == True and cond2 == True and cond3 == True and cond4 == True:
                return True
            elif cond1 == False and cond2 == False:
                return False
            elif cond3 == False and cond4 == False:
                return False
            
            # else :
            #     return True
    
    def set_zone(self, zone):
        self.zone = zone
    def set_road(self):
        self.road = True
    def build_road(self):
        if self.road == True:
            self.color  = (128, 128, 128)
    
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        