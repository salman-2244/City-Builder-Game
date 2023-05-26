import pygame as pygame
import sys
sys.path.append('./Zones')
from zone import Zone
#COST IS FLOAT SO IS THE MAINTANNCE FEE
    
class Forest():
    """
    Forest class
    """
    def __init__(self,id, year, zone, City):
        self.id = id
        self.year = year
        self.zone = zone
        self.radius = 150
        self.age = 0
        self.cost = 10
        self.maintainance = 20
        # self.picture = pygame.image.load("forest.png")
        self.happy=0
        self.seenBy = self.seen_By(City)
    
    def seen_By(self, City): # can be called periodcilly
        """
        _description_

        Args:
            fields (list): list of fields

        Returns:
            _type_: list of tuples
        by which fields is the forest seen
        """
        cnt = 0
        for field in City.zones:
            if field.x in range(self.zone.x, self.zone.x+self.radius) and field.y in range(self.zone.y, self.zone.y+self.radius):
                print("Tree here 1")
                
                print(f"field.x, field.y, {field.x}, {field.y}, {field.typ}")
                print(f"range {range(self.zone.x, self.zone.x+self.radius)}, {range(self.zone.x, self.zone.x+self.radius)}")
                if field.typ == "residential":
                    print("Tree here 2")
                    cnt += 1
        return cnt
    
    
    def grow(self, currentYear, City):
        """_summary_

        Args:
            currentYear (date): the current year
            City (City): the city object
            
        grows the forest by year
        """
        if (currentYear - self.year) > 0 and (currentYear - self.year) < 10:
            City.bank -= self.maintainance
        else:
            pass
        
    # use the reachables from the fields
    def reduceImpact(self, fields, City):
        """_summary_

        Args:
            fields (list of fields): list of fields
            City (City): the city object
            Reduce the impact of the industrial zones on the happiness of the residents
        """
        reach = []
        fld = self.zone
        cond1 = False; cond2 = False; cond3 = False; cond4 = False
        if len(fields) > 0:
            for field in fields:
                if (field.y == fld.y and (field.x in range(fld.x, fld.x+50))):
                    cond2 = True
                if (field.x == fld.x and (field.y in range(fld.y, fld.y+50))):
                    cond1 = True
                if (field.y == fld.y and (field.x in range(fld.x-50, fld.x))):
                    cond3 = True
                if (field.x == fld.x and (field.y in range(fld.y-50, fld.y))):
                    cond4 = True
        if cond1 and cond3:
            City.happiness += 5
        elif cond2 and cond4:
            City.happiness += 5
        else:
            pass  
        
    # def instantiate(self):
    #     self.              

