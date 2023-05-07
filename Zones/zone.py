import pygame   # import pygame library
import json
import sys
sys.path.append('./my_game')
from Citizen import Citizen
import random
import math
from Field import Field
# from my_game.City import City


# each zone is reppresented by a rectangle and buildings are drawn on top of it

class Zone:
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
        self.building = "" # the building that is built on top of the zone
    
    def searchForZones(self, City, type): # search for zones of a type
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
    
    
    
class residential(Zone):
    def __init__(self, name, cost, no):
        super().__init__(name, cost)
        #self.color = (0, 255, 0) 
        self.width = 0
        self.height = 0
        self.residents = [] # list of residents, residents are dictionaries or classes
        self.max_residents =  ((self.width * self.height) / 900) * 4 # max 4 residents per square
        self.num = no # number of the zone, used for saving and loading, ege Res1, Res2, Res3, etc.
        self.type = "residential"
        self.accesible = False
        self.constructed = False
        self.time_elapsed_since_last_action = 0
        self.building = "Zones/Assets/house.png"
        self.workerZones = set()
        self.reachable = set()
        
        
    def isRoad(self, City):
        for road in City.roads:
            if road.x in range(self.x -105, self.x+105) and road.y in range(self.y -101, self.y+101):
                self.accesible = True
                
                return True
    

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
        # print("Area:")
        # print(area)
        return (area / (50*50)) * 2 # 2 residents per square

    def deductPrice(self, City):
        City.bank -= self.cost
    
    
    def createInitialResidents(self, City): # each zone will have its own dictionary of residents
        id = 0 
        size = int(self.initialResidents())
        # print(f"Size: {size}")
        job = ""
        salary = 0
        for i in range(size):
            id+=1
            resident = Citizen(id, "", salary, 40,self.num)
            self.residents.append(resident)
        City.population += size
        if not self.isRoad(City):
            City.happiness -= 5   
        
        
    def getTaxes(self, City):# by traversing through the residents, get the taxes based on their salary
        tax = City.tax # tax rate
        for resident in self.residents:
            City.bank += round(resident.salary * (tax / 100))
            print("Tax: " + str(resident.salary * (tax / 100)))
    
    # def getHapiness(self):
    #     sum = 0
    #     for res in self.residents:
    #         sum += res.happy
    #     return sum / len(self.residents)
    
    def countResidents(self):
        return len(self.residents)
    def getHapiness(self):
        hapiness = 0
        for resident in self.residents:
            hapiness += resident.happy
        return (hapiness / len(self.residents)/2)
    
    def checkUnemployed(self):
        cnt = 0
        for resident in self.residents:
            if resident.job == "":
                cnt += 1
        return cnt
    
    def checkConnetcions(self, City, fields):
        # if self.isRoad(City) == True:
        #     for resident in self.residents:
        #         if resident.workZone != None:
        #             self.workerZones.add(resident.workZone)
        #             print(f"Added work zone {resident.workZone}")
            # check whether the residents have a connection to a work zone
            if self.isRoad(City) == True:
                for fld in fields:
                    connections = fld.connectsTo()
                    if connections != None:
                        for connection in connections:
                                for zone in City.zones:
                                    if zone.x in range(connection[0]-55, connection[0]+55) and zone.y in range(connection[1]-55, connection[1]+55) and zone.type != "residential":
                                        if zone.num not in self.reachable:
                                            self.reachable.add(zone.num)
                                            print(f"Added reachable zone {zone}")
                                            break
                
            
            
                    
            
    
    
    def moveOut(self, City):
        if len(self.residents) > 5:
            resNum = random.randint(0, len(self.residents)-1)
            res = self.residents[resNum]
            if res.workZone != None:
                for zone in City.zones:
                    if zone.num == res.workZone:
                        zone.removeEmployee(res)
                        break
            self.residents.remove(res)
            City.population -= 1
            # print("Moved out")
        
    def searchForWork(self, City, emp):
        for zone in City.zones:
            if zone.type == "industrial" or zone.type == "commercial" and zone.num in self.reachable:
                if len(zone.employees) < zone.max_employees:
                    emp.salary = random.randint(500, 1000)
                    emp.workZone = zone.num
                    zone.addEmployee(emp)
                    break
    
    def moveIn(self, City):
        cond = False
        if len(self.residents) == self.max_residents:
            print("Max residents reached for this zone")
            
        else:
            id = len(self.residents) + 1
            res = Citizen(id, "", 0, 40,self.num)
            self.residents.append(res)
            self.searchForWork(City, res)
            # print("Moved in")
            cond = True
            City.population += 1
        return cond
                
                
class inudstrial(Zone):
    def __init__(self, name, cost,num):
        super().__init__(name, cost)
        #self.color = (0, 0, 255)
        self.width = 0
        self.height = 0
        self.factories = []
        self.employees = [] # change in UML
        self.max_employees = 0
        self.type = "industrial"
        self.num = num
        self.constructed = False
        self.accessible = False
        self.building = " "
        
    def getName(self):
        return "Industrial"

    def setMaxEmployees(self):
        area = self.width * self.height
        emp = area / 250
        self.max_employees = emp * 3 # 3 employees per square
    def getMaxEmployees(self):
        return self.max_employees
    def addEmployee(self, employee):
        self.employees.append(employee)
    def removeEmployee(self, employee):
        self.employees.remove(employee)
    def getEmployees(self):
        return self.employees
    def rect_distance( self,l1, l2):
        x1 = l1[0]; y1 = l1[1];x1b = l1[2]; y1b = l1[3]
        x2 = l2[0]; y2 = l2[1];x2b = l2[2]; y2b = l2[3]
       
        left = x2b < x1
        right = x1b < x2
        bottom = y2b < y1
        top = y1b < y2
        if top and left:
            return math.dist((x1, y1b), (x2b, y2))
        elif left and bottom:
            return math.dist((x1, y1), (x2b, y2b))
        elif bottom and right:
            return math.dist((x1b, y1), (x2, y2b))
        elif right and top:
            return math.dist((x1b, y1b), (x2, y2))
        elif left:
            return x1 - x2b
        elif right:
            return x2 - x1b
        elif bottom:
            return y1 - y2b
        elif top:
            return y2 - y1b
        else:             # rectangles intersect
            return 0.
    def satsifaction(self, City):
        for zone in City.zones:
            if zone.type == "residential" and zone.accesible == True and self.num in zone.reachable:
                # print("here 1")
                resX = zone.x
                resY = zone.y
                resWidth = zone.width
                resHeight = zone.height
                distance = self.rect_distance((self.x, self.y, self.x + self.width, self.y + self.height), (resX, resY, resX + resWidth, resY + resHeight))
                if distance < 100:
                    City.happiness -= 2
                else:
                    City.happiness += 5
                

    def addWorkers(self, City):
        self.setMaxEmployees()
        # residential = self.searchForZones(City, "residential")
                # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        """Discuss this logic with the team""" 
        for zone in City.zones:
            if zone.type == "residential" and zone.accesible == True and self.num in zone.reachable:
                print("here 1")
                resX = zone.x
                resY = zone.y
                resWidth = zone.width
                resHeight = zone.height
                distance = self.rect_distance((self.x, self.y, self.x + self.width, self.y + self.height), (resX, resY, resX + resWidth, resY + resHeight))
                r = 0;
                # rands = random.sample(range(), 10)
                for resident in zone.residents:
                    r+=1
                    # res = random.randint(i, len(zone.residents)/2)
                    if resident.workZone == "" and resident.salary == 0 and len(self.employees) <= self.max_employees:
                        print("here 2" )
                        resident.workZone = self.num
                        sal = random.randint(500, 800)
                        resident.job = self.name
                        resident.salary = sal
                        resident.dist_to_work = distance
                        if sal < 600:
                             City.happiness -= 1
                        else:
                             City.happiness += 2
                        self.employees.append(resident)
                        # print(f"work: {resident.job } salary: {resident.salary} len: {len(self.employees)} max: {self.max_employees}")

            else:
                print("No more workers needed")
                pass; # do nothing
        for emp in self.employees:
            print(str(emp.id)+ " employed at " + self.name)
    
    
    def isRoad(self, City):
        for road in City.roads:
            if road.x in range(self.x -105, self.x+105) and road.y in range(self.y -101, self.y+101):
                self.accesible = True
                return True
    
    
    
class general(Zone): #roads, change in UML
    def __init__(self, name, cost,num):
        super().__init__(name, cost)
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
        self.constructed = False
        Zone.num = num
        self.police = False
        self.stadium = False
        self.radius = 5
        self.max_police_station = 0
        self.max_stadium = 0
        self.policeStations = []
        self.stadiums = []
        self.maxWoker = 0
        self.road = False
        
    def setMaxWorker(self ):
        if self.name != "Road" or self.name != "Forest":
            if self.police == True or self.stadium == True:
                self.maxWorker = 100
            elif self.police == True and self.stadium == True:
                self.maxWorker = 150
                
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
    
    def inRadius(self, zone):
        if zone.x > self.x - self.radius and zone.x < self.x + self.width + self.radius and zone.y > self.y - self.radius and zone.y < self.y + self.height + self.radius:
            return True
    
    # use this for radius happiness 
    def increaseHappyRadius(self, City):
        for zone in City.zones:
           if zone.type == "residential":
            if self.inRadius(zone):
                City.happiness += 1
    
    
    def satsifaction(self, City):
        if self.police == True or self.stadium == True:
            for zone in City.zones:
                    if zone.type == "residential" and zone.accesible == True and self.num in zone.reachable:
                        print("here 1")
                        resX = zone.x
                        resY = zone.y
                        resWidth = zone.width
                        resHeight = zone.height
                        distance = self.rect_distance((self.x, self.y, self.x + self.width, self.y + self.height), (resX, resY, resX + resWidth, resY + resHeight))
                        if distance < 100:
                            City.happiness -= 2
                        else:
                            City.happiness += 5
    
    
    def addWorkers(self, City):
        if self.police == True or self.stadium == True: 
            for zone in City.zones:
                if zone.type == "residential" and zone.accesible == True:
                    # print("here 1")
                    resX = zone.x
                    resY = zone.y
                    resWidth = zone.width
                    resHeight = zone.height
                    distance = self.rect_distance((self.x, self.y, self.x + self.width, self.y + self.height), (resX, resY, resX + resWidth, resY + resHeight))
                    r = 0;
                    # rands = random.sample(range(), 10)
                    for resident in zone.residents:
                        r+=1                        
                        if resident.workZone == "" and resident.salary == 0 and len(self.employees) <= self.max_employees:
                                 print("here 2" )
                        resident.workZone = self.num
                        sal = random.randint(500, 800)
                        resident.job = self.name
                        resident.salary = sal
                        resident.dist_to_work = distance
                        if sal < 600:
                             City.happiness -= 1
                        else:
                             City.happiness += 2
                        self.employees.append(resident)
                        print(f"work: {resident.job } salary: {resident.salary} len: {len(self.employees)} max: {self.max_employees}")

            else:
                print("No more workers needed")
                pass; # do nothing
        for emp in self.employees:
            print(str(emp.id)+ " employed at " + self.name)
    
    def isRoad(self, City):
        # print("Checking for road")
        for road in City.roads:
            # print("Road: " + str(road.x) + " " + str(road.y))
            # print("Res: " + str(self.x) + " " + str(self.y))
            if road.x in range(self.x -105, self.x+105) and road.y in range(self.y -101, self.y+101):
                self.accesible = True
                # print("Road found")
                
                return True
    
#creating the service zone
class service(Zone):
    def __init__(self, name, cost,num):
        super().__init__(name, cost)
        #self.color = (255, 0, 0)
        self.width = 0
        self.height = 0
        self.employees = []
        
        self.type = "service"
        self.num = num
        self.constructed = False
        self.accessible = False
        self.building = "Zones/Assets/comm.png"
    
    def rect_distance( self,l1, l2):
        x1 = l1[0]; y1 = l1[1];x1b = l1[2]; y1b = l1[3]
        x2 = l2[0]; y2 = l2[1];x2b = l2[2]; y2b = l2[3]
       
        left = x2b < x1
        right = x1b < x2
        bottom = y2b < y1
        top = y1b < y2
        if top and left:
            return math.dist((x1, y1b), (x2b, y2))
        elif left and bottom:
            return math.dist((x1, y1), (x2b, y2b))
        elif bottom and right:
            return math.dist((x1b, y1), (x2, y2b))
        elif right and top:
            return math.dist((x1b, y1b), (x2, y2))
        elif left:
            return x1 - x2b
        elif right:
            return x2 - x1b
        elif bottom:
            return y1 - y2b
        elif top:
            return y2 - y1b
        else:             # rectangles intersect
            return 0.
        
    def setAndDraw(self, screen, city ,pos, tiles): 
            for tile in tiles:
                if pos[0] in range (tile.x +50) and pos[1] in range (tile.y +50):
                    self.x = tile.x
                    self.y = tile.y
                    self.width = 50
                    self.height = 50
                    self.constructed = True
                    image = pygame.image.load(self.building)
                    screen.blit(image, (self.x + 10, self.y + 10))
                    # self.deductPrice(city) # when draw the zone, deduct the price from the bank
                    return True
            return False
            
        
    def satsifaction(self, City):
        for zone in City.zones:
            if zone.type == "residential" and zone.accesible == True and self.num in zone.reachable:
                print("here 1")
                resX = zone.x
                resY = zone.y
                resWidth = zone.width
                resHeight = zone.height
                distance = self.rect_distance((self.x, self.y, self.x + self.width, self.y + self.height), (resX, resY, resX + resWidth, resY + resHeight))
                if distance < 100:
                    City.happiness -= 2
                else:
                    City.happiness += 5    
    
    
    
    def addWorkers(self, City):
        residential = self.searchForZones(City, "residential")
                # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        """Discuss this logic with the team""" 
        for zone in City.zones:
            if zone.type == "residential" and zone.accesible == True:
                # print("here 1")
                resX = zone.x
                resY = zone.y
                resWidth = zone.width
                resHeight = zone.height
                distance = self.rect_distance((self.x, self.y, self.x + self.width, self.y + self.height), (resX, resY, resX + resWidth, resY + resHeight))
                r = 0;
                # rands = random.sample(range(), 10)
                for resident in zone.residents:
                    r+=1
                    # res = random.randint(i, len(zone.residents)/2)
                    
                    if resident.workZone == "" and resident.salary == 0 and len(self.employees) <= self.max_employees:
                        print("here 2" )
                        resident.workZone = self.num
                        sal = random.randint(500, 800)
                        resident.job = self.name
                        resident.salary = sal
                        resident.dist_to_work = distance
                        if sal < 600:
                             City.happiness -= 1
                        else:
                             City.happiness += 2
                        self.employees.append(resident)
                        print(f"work: {resident.job } salary: {resident.salary} len: {len(self.employees)} max: {self.max_employees}")

            else:
                print("No more workers needed")
                pass; # do nothing
        for emp in self.employees:
            print(str(emp.id)+ " employed at " + self.name)
    
    def isRoad(self, City):
        # print("Checking for road")
        for road in City.roads:
            # print("Road: " + str(road.x) + " " + str(road.y))
            # print("Res: " + str(self.x) + " " + str(self.y))
            if road.x in range(self.x -105, self.x+105) and road.y in range(self.y -101, self.y+101):
                self.accesible = True
                # print("Road found")
                
                return True
