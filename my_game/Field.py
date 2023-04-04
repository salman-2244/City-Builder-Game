from Zones.zone import Zone
class Field:
    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.size = size # size of the individual tile
        self.zone = None # zone , when selcted change to the zone it is in
        self.road = False # bool to check if there is a road on the field
        
    def set_zone(self, zone):
        self.zone = zone
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        