class City:
    def __init__(self, name, tax, happiness):
        self.name = name
        self.tax = tax
        self.happiness = happiness
        self.population = 0
        # self.citizens = []
        # self.zones = []
        # self.roads = []
        self.bank = 200000
        self.zones = []
        self.roads = []
        
    # def citizensMovingIn(self, citizen):
    #     for i in range(len(self.zones)):
    #         if self.zones[i].id == "residential":
    #             self.zones[i].citizens.append(citizen)
    #             self.population += 1
    #             break
            
            
    # def citizensMovingOut(self, citizen):
    #     for i in range(len(self.zones)):
    #         if self.zones[i].id == "residential":
    #             self.zones[i].citizens.remove(self.zones[i].citizens[len(self.zones[i].citizens)-2])
    #             self.population -= 1
    #             break
    
    # def taxMoney(self):
    #     for i in range(len(self.zones)):
    #         if self.zones[i].id == "residential":
    #             for j in range(len(self.zones[i].citizens)):
    #                 self.bank += self.zones[i].citizens[j].salary * (self.tax/100)
    #             break
            

            
    
        
    
    