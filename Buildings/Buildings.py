import pygame as pygame
import Zones.zone as zone

#COST IS FLOAT SO IS THE MAINTANNCE FEE
class Building():
    def __init__(self, name,x, y, width, height, cost):
        self.__x = x
        self.__y = y
        self.__width = width
        self.__height = height
        self.__location = zone
        self.__name = name
        self.cost = cost
        
    
    
    """I dont know what to do with this, or to delete it"""
    def draw(self, window):
        pygame.draw.rect(window, self.color, (self.x, self.y, self.width, self.height))

# class House(Building):
#         def __init__(self, name, x, y, width, height, location, cost):
#             super().__init__(name, x, y, width, height, location, cost)
#             self.__color = 0
#             self.__residents = []
#             self.__max_residents = 5
#             self.__cost = 0
#             self.__picture = pygame.image.load("house.png") # load the image, change the path to the image
#             self.__picture = pygame.transform.scale(self.picture, (self.width, self.height)) # scale the image to the size of the house
#             self.__x = 0 # initial
#             self.__y = 0 # initial
#         """def addResident(self, resident):
#             self.residents.append(resident)
#         def removeResident(self, resident):
#             self.residents.remove(resident)"""
#         def set_position(self, coordinates): # pass tuple
#             self.__x = coordinates[0]
#             self.__y = coordinates[1]
#         def get_capacity(self) :
#             return self.__max_residents

#         def draw(self, window):
#             window.blit(self.picture, (self.x, self.y))


# class Service_Building(Building):
#     def __init__(self, name, x, y, width, height, location, cost):
#         super().__init__(name, x, y, width, height, location, cost)
#         self.__res = 0
#         self.__maxRes = x*y*2
#     def build(self, window):
#         window.blit(self.picture, (self.__x, self.__y))
#     def demolish(self, window): # removing the image from the window
#         self.image.fill((0,0,0,0)) # fill the image of the building with transparent
#     def upgrade(self): # what is meant by this check???
#         pass
#     def calculate_maintnance(self):
#         return self.__res / self.__maxRes * 10
#     def get_intersection(self): # ???
#         pass
#     def getWid(self):
#         return self.__width
#     def getHeight(self):
#         return self.__height
#     def accesible(self): # retrurn bool once the road class is created !!
        # pass

class Road(Building):
        def __init__(self, name, x, y, width, height, location, cost):
            super().__init__(name, x, y, width, height, location, cost)
            self.__maintenance_fee = 0
            self.__public_accessible = False
            self.__orientation = "-"
        # def draw(self, window):
        #     window.blit(self.picture, (self.__x, self.__y))
        def demolish(self, window): # removing the image from the window
            self.image.fill((0,0,0,0)) # fill the image of the building with transparent
        def calculate_maintnance(self):
            return self.__cost / 10
        def implementFee(self, city):
            city.bank -= self.calculate_maintnance()
        def get_intersetcion(self): # collision of rhe rect
            #if self.rect.colliderect()get from the tiles 2d array
            pass
        def getWid(self):
            return self.__width
        def getHeight(self):
            return self.__height
        def get_dir(self):
            return self.__orientation
        def accesible(self): # retrurn bool once the road class is created !!
            pass

class Police(Building):
        def __init__(self, name, x, y, width, height, location, cost):
            super().__init__(name, x, y, width, height, location, cost)
            self.__picture = pygame.image.load("police.png") # load the image, change the path to the image
            self.__publicSaftey = 10 # public saftey points
            self.__radius = 2; #2x2 tiles


        def build(self, window):
            window.blit(self.picture, (self.__x, self.__y))
        #def demolish(self, window):
        def get_saftey(self): # return the public saftey points
            return self.__publicSaftey
        def get_radius(self):
            return self.__radius
        def moreHappy(self): # increase the happiness of the residents
            pass
        
   
   # stadium class
class Stadium(Building):
        def __init__(self, name, x, y, width, height, location, cost):
            super().__init__(name, x, y, width, height, location, cost)
            self.__picture = pygame.image.load("stadium.png")
            self.__radius = 2 # 2x2 tiles
            self.__bonus = 5 # bonus for the happiness of the residents
            # maybe not needed DISCUSS! self.revenue = 0 # revenue from the stadium at the beggining
        
        
        def build(self, window, zone):
            if zone.get_type() == "general":
                window.blit(self.picture, (self.__x, self.__y))
            # window.blit(self.picture, (self.__x, self.__y))
        def get_radius(self):
            return self.__radius
        def get_bonus(self):
            return self.__bonus
    
# class Forest(Building):
#         def __init__(self, name, x, y, width, height, location, cost):
#             super().__init__(name, x, y, width, height, location, cost)
#             self.__picture = pygame.image.load("forest.png")
#             self.__radius = 3 # 3x3 tiles at the beggining, we will make it grow year by year
#             self.__age = 0 # age of the forest at the beggining
#             self.__maintainance = 20 # maintainance fee for the forest, PER MONTH
#         def build(self, window):
#             window.blit(self.picture, (self.__x, self.__y))
#         def get_radius(self):
#             return self.__radius
#         def get_age(self):
#             return self.__age
#         def get_maintainance(self):
#             return self.__maintainance
#         def grow(self): # grows by year, not by trees
#             self.__radius += 1
#             self.__maintainance += 10
#             if self.__age < 10:
#                 self.__age += 1
#             elif self.__age >= 10:
#                 pass
#         def calculate_maintnance(self):
#             self.__maintainance *= 10 
#         def get_maintainance(self):
#             return self.__maintainance
    
    
class Forest():
    def __init__(self,id, year, zone, fields):
        self.id = id
        self.year = year
        self.zone = zone
        self.radius = 150
        self.age = 0
        self.cost = 10
        self.maintainance = 20
        # self.picture = pygame.image.load("forest.png")
        self.happy=0
        self.seenBy = self.seen_By(fields)
    
    def seen_By(self, fields): # can be called periodcilly
        seenby = []
        for field in fields:
            if field. x in range(self.zone.x, self.zone.x+self.radius) and field.y in range(self.zone.y, self.zone.y+self.radius):
                if field.zone.typ == "Residential" and (field.x, field.y) not in seenby:
                    seenby.append((field.x, field.y))
        return seenby
    
    
    def grow(self, currentYear, City):
        if (currentYear - self.year) > 0 and (currentYear - self.year) < 10:
            City.bank -= self.maintainance
        else:
            pass
        
    # use the reachables from the fields
    def reduceImpact(self, fields, City):
        reachables = []
        fld = None
        for field in fields:
            if field.x == self.zone.x and field.y == self.zone.y:
                fld = field
                break
        if fld != None:
            reachables = fld.connectsTo()
        cond1 = False; cond2 = False; 
        for field in fields:
            if (field.x == fld.x and (field.y in range(fld.y, fld.y+50) or (field.y in range(fld.y, fld.y-50)))):
                cond1 = True
            elif (field.y == fld.y and (field.x in range(fld.x, fld.x+50) or (field.x in range(fld.x, fld.x-50)))):
                cond2 = True
        if cond1 and cond2:
            City.happiness += 5
        else:
            pass                

