# from Zones.zone import zone
import pygame as pg

"""_summary_

    Returns:
        _type_: _description_
        Class for the fields on the grid
        
    """
import pygame as pg

class Field:
    """Class for the fields on the grid."""

    def __init__(self, x, y, size):
        """
        Initialize a Field object.

        Args:
            x (int): X-coordinate of the field in the 2D array.
            y (int): Y-coordinate of the field.
            size (int): Size of the individual tile.
        """
        self.x = x
        self.y = y
        self.size = size
        self.grid_pos = None
        self.color = (86, 148, 70)
        self.building = ""
        self.img = None
        self.Bimg = None
        self.zone = None # zone , when selcted change to the zone it is in
        self.road = False  # bool to check if there is a road on the field, if true make the color grey over the background
        self.selected = False # Holds if the field is selected or not
        self.rect = pg.Rect(self.x, self.y, self.size, self.size)  # drawing rect on grid
        self.id = None
        self.image_rect = None

    def getX(self):
        """
        Get the X-coordinate of the field.

        Returns:
            int: The X-coordinate of the field.
        """
        return self.x

    def connectsTo(self):
        """
        Check if the field connects to other fields.

        Returns:
            list: A list of coordinate tuples representing reachable fields.
        """
        if self.road:
            reachables = [(self.x, self.y + 55), (self.x, self.y - 55), (self.x + 55, self.y), (self.x - 55, self.y)]
            return reachables

    def destructible(self, fields):
        """
        Check if the field is destructible.

        Args:
            fields (list): A list of Field objects.

        Returns:
            bool: True if the field is destructible, False otherwise.
        """
        cond1 = True
        cond2 = True
        cond3 = True
        cond4 = True
        unzoned = True

        if self.road and self.zone.typ == "general":
            for field in fields:
                if self.y + 50 == field.y and field.x == self.x and field.road:
                    cond1 = False
                if self.y + 50 == field.y and field.x == self.x and field.zone.typ != "general":
                    unzoned = False
                if self.y - 50 == field.y and field.x == self.x and field.road:
                    cond2 = False
                if self.y - 50 == field.y and field.x == self.x and field.zone.typ != "general":
                    unzoned = False
                if self.x + 50 == field.x and field.y == self.y and field.road:
                    cond3 = False
                if self.x + 50 == field.x and field.y == self.y and field.zone.typ != "general":
                    unzoned = False
                if self.x - 50 == field.x and field.y == self.y and field.road:
                    cond4 = False
                if self.x - 50 == field.x and field.y == self.y and field.zone.typ != "general":
                    unzoned = False
            if not unzoned:
                return False
            if cond1 and cond2 and cond3 and cond4:
                return True
            elif not cond1 and not cond2:
                return False
            elif not cond3 and not cond4:
                return False

    def set_zone(self, zone):
        """
        Set the zone of the field.

        Args:
            zone: The zone object to set for the field.
        """
        self.zone = zone

    def set_road(self):
        """Set the road attribute of the field to True."""
        self.road = True
    
