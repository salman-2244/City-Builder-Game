import pygame   # import pygame library
import json



class zone:
    def __init__(self, name, cost, type):
        self.name = name
        self.__cost = cost
        self.__type = type
        self.__color = (0, 0, 0)
        self.__x = 0
        self.__y = 0
        self.__width = 0
        self.__height = 0
    
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
    def __init__(self, name, cost, type):
        super().__init__(name, cost, type)
        #self.color = (0, 255, 0) 
        self.width = 0
        self.height = 0
        self.residents = {} # dictionary of residents
        self.max_residents =  ((self.width * self.height) / 900) * 4 # max 4 residents per square

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
        return (self.area / 900) * 2 # 2 residents per square
    
    def createInitialResidents(self): # each zone will have its own dictionary of residents
        size = self.initialResidents()
        job = ""
        for i in range(size):
            if i % 3 ==0:
                job = "office" # works in office 
            else:
                job = "factory" # facotry worker
            resident = {"resident" : i, "job" : job, "satisfaction" : 50} # intial satisfaction is 50%
            self.residents.update(resident)


class inudstrial(zone):
    def __init__(self, name, cost,type):
        super().__init__(name, cost, type)
        #self.color = (0, 0, 255)
        self.width = 0
        self.height = 0
        self.factories = {}
        self.employees = {} # change in UML
        self.max_employees = 0

    def setMaxEmployees(self, max_employees):
        self.max_employees = max_employees
    def getMaxEmployees(self):
        return self.max_employees
    def addEmployee(self, employee):
        self.employees.update(employee)
    def removeEmployee(self, employee):
        self.employees.remove(employee)
    def getEmployees(self):
        return self.employees
    
class general(zone): #roads, change in UML
    def __init__(self, name, cost, type):
        super().__init__(name, cost, type)
        #self.color = (0, 0, 0)
        
        self.width = 0
        self.height = 0
        self.roads = {}
        self.max_roads = 0
        self.max_forests = 0
        self.forests = {}
        self.police = 0
        self.stadium = 0
    
    def setMaxRoads(self, max_roads):
        self.max_roads = max_roads
    def setMaxForests(self, max_forests):
        self.max_forests = max_forests
    def getMaxRoads(self):
        return self.max_roads
    def getMaxForests(self):
        return self.max_forests
    def addRoad(self, road):
        self.roads.update(road)
    def addForest(self, forest):
        self.forests.update(forest)
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
        self.policeStations = {}
        self.stadiums = {}
    
    def setMaxPoliceStation(self, max_police_station):
        self.max_police_station = max_police_station
    def setMaxStadium(self, max_stadium):
        self.max_stadium = max_stadium
    def getMaxPoliceStation(self):
        return self.max_police_station
    def getMaxStadium(self):
        return self.max_stadium
    def addPoliceStation(self, policeStation):
        self.policeStations.update(policeStation)
    def addStadium(self, stadium):
        self.stadiums.update(stadium)
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