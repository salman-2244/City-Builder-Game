import random

class City:

    def __init__(self, name, tax, happiness):
        """_summary_

        Args:
            name (String): _description_
            tax (int): _description_
            happiness (int ): _description_
        """
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
        self.forests = []
        
    
    def citizensMovingIn(self, citizen):
        """_summary_

        Args:
            citizen (Citizen): Takes citizenc class object as an argument
            Citizens move in to the city and the population increases by 1
        """
        for i in range(len(self.zones)):
            if self.zones[i].id == "residential":
                self.zones[i].citizens.append(citizen)
                self.zones[i].maxCitizens += 1
                self.population += 1
                break
            
            
    def citizensMovingOut(self):
        """
        Citizens move out of the city and the population decreases by 1
        """
        if self.happiness < 60:
            for i in range(len(self.zones)):
                if self.zones[i].id == "residential":
                    self.zones[i].citizens.remove(self.zones[i].citizens[len(self.zones[i].citizens)-2])
                    self.population -= 3
                    self.zones[i].maxCitizens -= 3
                break
    
    def maintnanceFee(self):
        """
        Maintnance fee for roads, police stations and stadiums
        """
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
        """_summary_

        Args:
            citizen (Citizen): Takes citizenc class object as an argument
            Randomly moves citizens in and out of the city
        """
        ran = random.randint(0, 1)
        if ran == 1:
            self.citizensMovingOut()
        else:
            self.citizensMovingIn(citizen)
    
    
    def taxMoney(self):
        """
        Tax money is added to the bank
        """
        for i in range(len(self.zones)):
            if self.zones[i].name == "res":
                for j in range(len(self.zones[i].residents)):
                    self.bank += self.zones[i].residents[j].salary * (self.tax/100)
        # print(f"added tax money {self.zones[i].residents[j].salary * (self.tax/100)}")
                break
            
    def happinessChange(self):
        """
        Happiness changes according to the tax rate
        """
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
        """
        Checks for employment periodically in the residential zones
        """
        print("Checking for employment >>>")
        for zone in self.zones:
            if zone.typ == "general":
               if zone.police or zone.stadium:
                   zone.addWorkers(self)
            elif zone.typ == "industrial":
                zone.addWorkers(self)
            elif zone.typ == "service":
                zone.addWorkers(self)
                
    # def periodicalHappy(self):
    #     pass
    #     # """_summary_

    #     # Returns:
    #     #     Int: Checks the happiness of the city and returnas an integer
    #     # """
    #     # sum = 0
    #     # cnt = 0
    #     # for zone in self.zones:
    #     #     if zone.typ == "residential":
    #     #         cnt += 1
    #     #         sum += zone.getHapiness()
    #     # if cnt == 0:
    #     #     return 50
    #     # return sum/cnt
    
    def periodicalTax(self):
        """
        Checks the tax rate of the city in the residential zones
        """
        sum = 0
        cnt = 0
        
        for zone in self.zones:
            if zone.typ == "residential":
                cnt+=1
                zone.getTaxes(self)
            if cnt == 0:
                pass
    
    
    def checkResidentialConnection(self, fields):
        """_summary_

        Args:
            fields (fields): fields class object
            Checks the connection of the residential zones through the fields classs
            
        """
        for zone in self.zones:
            if zone.typ == "residential":
                zone.checkConnetcions(self,fields)
                
    def moveInAndOut(self):
        """
        Moves citizens in and out of the city according to the happiness
        """
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
                
    def maintainForests(self, year):
        """_summary_

        Args:
            year (year): date
            Maintains the forests
        """
        for forest in self.forests:
            forest.grow(year, self)

    def forestImpact(self, fields):
        """_summary_

        Args:
            fields (field)): fields class object
            Reduces the impact with the forests presence
        """
        for forest in self.forests:
            forest.reduceImpact(fields, self)
    
    def helpCitizens(self, fields):
        """_summary_
        Help citizens with seeing the forest
        """
        seenBy = []
        if len(self.forests) > 0:        
            for forest in self.forests:
                seenBy = forest.seen_By(fields)
                print(len(seenBy))
                if seenBy != []:
                    self.happiness += round(len(seenBy) * 0.5)
            
            
    
            
        
            
                    
               
    
        
    
    