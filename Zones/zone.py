import pygame   # import pygame library
import json
import sys
sys.path.append('./my_game')
from Citizen import Citizen
import random
# from my_game.City import City


class zone:
    def __init__(self, name, cost):
        self.name = name
        self.cost = cost
        # self.type = type
        self.color = (0, 0, 0)
        self.x = 0
        self.y = 0
        self.width = 0
        self.height = 0
        self.accessible = False # if the zone is accessible to the road, set this in function
    
    def searchForNZones(self, City, type):
        cands = []
        for cand in City.zones:
            if cand.type == type and cand.accessible == True:
             # return the nearest zone of the type
                cands.append(cand)
        if len(cands) == 0:
            return None
        else :
            return cands
       
            
    
    def setXY(self, x, y):
        self.x = x
        self.y = y

    def build(self, win): # drwaing the zone
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height))

    def reclassify(self, type):
        self.type = type
    
    def setSaturation(self, saturation):
        self.saturation = saturation

    def setCapacity(self, capacity):
        self.capacity = capacity
    
    def getCapacity(self):
        return self.capacity
    
    def getSaturation(self):
        return self.saturation

    def __str__(self):
        return self.name + " " + str(self.x) + " " + str(self.y) + " " + str(self.width) + " " + str(self.height) + " " + str(self.color)
    
class residential(zone):
    def __init__(self, name, cost, no):
        super().__init__(name, cost)
        #self.color = (0, 255, 0) 
        self.width = 0
        self.height = 0
        self.residents = [] # list of residents, residents are dictionaries or classes
        self.max_residents =  ((self.width * self.height) / 900) * 4 # max 4 residents per square
        self.no = no # number of the zone, used for saving and loading, ege Res1, Res2, Res3, etc.
        self.type = "residential"

    def getName(self):
        return "Residential"

    def drawImg(self, screen):
        pass; 
    def addResident(self, resident):
        self.residents.update(resident)
    def removeResident(self, resident):
        self.residents.remove(resident)
    def getResidents(self):
        return self.residents
    def initialResidents(self):
        area = self.width * self.height
        print("Area:")
        print(area)
        return (area / (50*50)) * 2 # 2 residents per square

    
    def createInitialResidents(self, City): # each zone will have its own dictionary of residents
        size = int(self.initialResidents())
        print(f"Size: {size}")
        job = ""
        salary = 0
        for i in range(size):
            resident = Citizen(id, "", salary, 50,self.no,)
            self.residents.append(resident)
        City.population += size    
        City.zones.append(self)
        
    def getTaxes(self, City):# by traversing through the residents, get the taxes based on their salary
        tax = City.tax # tax rate
        for resident in self.residents:
            City.bank += resident.salary * (tax / 100)
    def countResidents(self):
        return len(self.residents)
    # how to check whether the zone is accessible to the road
    def isAcessible(self, city_tiles):
        if self.accesible == False:
            #find the residential zone in the city tiles
            for c in city_tiles:
                if (c.x in range(self.x + 50, (self.x + self.width + 50)) and c.y in range(self.y + 50, (self.y + self.height + 50))) or (c.x in range(self.x - 50, (self.x + self.width - 50)) and c.y in range(self.y - 50, (self.y + self.height - 50))) or (c.x in range(self.x + 50, (self.x + self.width + 50)) and c.y in range(self.y - 50, (self.y + self.height - 50))) or (c.x in range(self.x - 50, (self.x + self.width - 50)) and c.y in range(self.y + 50, (self.y + self.height + 50))) and c.type == "road": # if the zone is next to the road 
                        self.accesible = True
                else:
                    self.accesible = False 
                """Test this tmrw"""
                  
        
        


class inudstrial(zone):
    def __init__(self, name, cost,type):
        super().__init__(name, cost, type)
        #self.color = (0, 0, 255)
        self.width = 0
        self.height = 0
        self.factories = []
        self.employees = [] # change in UML
        self.max_employees = 0
        self.type = "industrial"

    def getName(self):
        return "Industrial"

    def setMaxEmployees(self):
        area = self.width * self.height
        emp = area / 2500 
        self.max_employees = emp * 3 # 3 employees per square
    def getMaxEmployees(self):
        return self.max_employees
    def addEmployee(self, employee):
        self.employees.append(employee)
    def removeEmployee(self, employee):
        self.employees.remove(employee)
    def getEmployees(self):
        return self.employees
    def addWorkers(self, City):
        residential = self.searchForNZones(City, "residenial")
        
        
        # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        """Discuss this logic with the team""" 
        
        # for zone in City.zones:
        #     if zone.type == "residential" :
        #         rands = random.sample(range(), 10)
        #         for i in len(zone.residents)/2:
        #             res = random.randint(i, len(zone.residents)/2)
                    
        #             if resident.job == "":
        #                 sal = random.randint(500, 800)
        #                 resident.job = self.name
        #                 resident.salary = sal
        #                 self.employees.append(resident)
        #                 break
        
    
class general(zone): #roads, change in UML
    def __init__(self, name, cost, type):
        super().__init__(name, cost, type)
        #self.color = (0, 0, 0)
        
        self.width = 0
        self.height = 0
        self.roads = []
        self.max_roads = 0
        self.max_forests = 0
        self.forests = []
        self.police = 0
        self.stadium = 0
        self.type = "general"
    
    def getMaxForests(self):
        return self.max_forests
    def addRoad(self, road):
        self.roads.append(road)
    def addForest(self, forest):
        self.forests.appen(forest)
    def removeRoad(self, road):
        self.roads.remove(road)
    def removeForest(self, forest):
        self.forests.remove(forest)
    def getRoads(self):
        return self.roads
    def getForests(self):
        return self.forests
    
#creating the service zone
class service(zone):
    def __init__(self, name, cost, type):
        super().__init__(name, cost, type)
        #self.color = (255, 0, 0)
        self.width = 0
        self.height = 0
        self.police = 0
        self.stadium = 0
        self.max_police_station = 0
        self.max_stadium = 0
        self.policeStations = []
        self.stadiums = []
        self.type = "service"
    
    def setMaxPoliceStation(self, max_police_station):
        self.max_police_station = max_police_station
    def setMaxStadium(self, max_stadium):
        self.max_stadium = max_stadium
    def getMaxPoliceStation(self):
        return self.max_police_station
    def getMaxStadium(self):
        return self.max_stadium
    def addPoliceStation(self, policeStation):
        self.policeStations.append(policeStation)
    def addStadium(self, stadium):
        self.stadiums.append(stadium)
    def removePoliceStation(self, policeStation):
        self.policeStations.remove(policeStation)
    def removeStadium(self, stadium):
        self.stadiums.remove(stadium)
    def getPoliceStations(self):
        return self.policeStations
    def getStadiums(self):
        return self.stadiums
    
    def setPolice(self, police):
        self.police = police
    def setStadium(self, stadium):
        self.stadium = stadium
    def getPolice(self):
        return self.police
    def getStadium(self):
        return self.stadium