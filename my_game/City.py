import random

class City:
    def __init__(self, name, tax, happiness):
        self.name = name
        self.tax = tax
        self.happiness = 50 # initial happiness
        self.population = 0
        # self.citizens = []
        # self.zones = []
        # self.roads = []
        self.polCnt = 0
        self.StadCnt = 0
        self.roadCnt = 0
        self.bank = 200000
        self.zones = []
        self.roads = []
        
    def citizensMovingIn(self, citizen):
        for i in range(len(self.zones)):
            if self.zones[i].id == "residential":
                self.zones[i].citizens.append(citizen)
                self.zones[i].maxCitizens += 1
                self.population += 1
                break
            
            
    def citizensMovingOut(self):
        if self.happiness < 60:
            for i in range(len(self.zones)):
                if self.zones[i].id == "residential":
                    self.zones[i].citizens.remove(self.zones[i].citizens[len(self.zones[i].citizens)-2])
                    self.population -= 3
                    self.zones[i].maxCitizens -= 3
                break
    
    def maintnanceFee(self):
        roadCnt = len(self.roads)
        
        self.bank -= roadCnt
            # print("road maintnance fee")
        
        if self.polCnt > 0:
            self.bank -= 100
            print("police maintnance fee")
        if self.StadCnt > 0:
            self.bank -= 200
            print("stadium maintnance fee")    
                    
    def randMove(self, citizen):
        ran = random.randint(0, 1)
        if ran == 1:
            self.citizensMovingOut()
        else:
            self.citizensMovingIn(citizen)
    
    
    def taxMoney(self):
        for i in range(len(self.zones)):
            if self.zones[i].name == "res":
                for j in range(len(self.zones[i].residents)):
                    self.bank += self.zones[i].residents[j].salary * (self.tax/100)
        # print(f"added tax money {self.zones[i].residents[j].salary * (self.tax/100)}")
                break
            
    def happinessChange(self):
        sum = 0
        for zone in self.zones:
            if(zone.name == "gen"):
                hap = 0
                for res in zone.residents:
                    hap+= res.happy
                hap = hap/len(zone.residents)
                sum += hap
        self.happiness = sum/len(self.zones) 
                    
    
    def employPeriodically(self):
        print("Checking for employment >>>")
        for zone in self.zones:
            if zone.typ == "general":
               if zone.police or zone.stadium:
                   zone.addWorkers(self)
            elif zone.typ == "industrial":
                zone.addWorkers(self)
            elif zone.typ == "service":
                zone.addWorkers(self)
                
    def periodicalHappy(self):
        sum = 0
        cnt = 0
        for zone in self.zones:
            if zone.typ == "residential":
                cnt += 1
                sum += zone.getHapiness()
        if cnt == 0:
            return 50
        return sum/cnt
    
    def periodicalTax(self):
        sum = 0
        cnt = 0
        
        for zone in self.zones:
            if zone.typ == "residential":
                cnt+=1
                zone.getTaxes(self)
            if cnt == 0:
                pass
    def checkResidentialConnection(self, fields):
        for zone in self.zones:
            if zone.typ == "residential":
                zone.checkConnetcions(self,fields)
                
    def moveInAndOut(self):
        for zone in self.zones:
            if zone.typ == "residential":
                if self.happiness < 50:
                    zone.moveOut(self)
                    zone.moveOut(self)
                    zone.moveOut(self)
                    if (zone.moveIn(self) == False):
                        continue
                if self.happiness > 50:
                    if (zone.moveIn(self) == False):
                        continue
                    else:
                        zone.moveIn(self)
                        zone.moveIn(self)
                    zone.moveOut(self)
    def changeZones(self,toChng, change):
        for zone in self.zones:
            if (zone.x == toChng.x and zone.y == toChng.y) and (change.x == toChng.x and change.y == toChng.y):
                zone = change
                break                 
                
                
            
                    
               
    
        
    
    