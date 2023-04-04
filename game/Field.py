from Zones.zone import Zone
class Field:
    def __init__(self, x, y, size, zone):
        self.x = x
        self.y = y
        self.size = size
        self.zone = None # zone , when selcted change to the zone it is in
        self.road = False # bool to check if there is a road on the field
        


