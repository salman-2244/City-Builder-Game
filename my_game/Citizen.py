#import the 

# Citizen class

class Citizen(): 
    def __init__(self, id, workZone, salary, happy, home):
        self.id = id
        self.workZone = workZone
        self.salary = salary
        self.happy = happy
        self.home = home
        # self.work = work
        self.homeCloseToWork = False
        self.dist_to_work = 0
        
        
    
    def toDict(self):
        return {"id": self.id, "workZone": self.workZone, "salary": self.salary, "happy": self.happy, "home": self.home}

    def calcHappy(self, salary, tax, distance):
        self.happy = (salary - (salary * (tax/100))) - (distance * 0.1)
        if distance == 0: # unemployed
            self.happy = 0
        if self.happy < 0: 
            self.happy = 0
        return self.happy
    # def isCloseWork(self, ) 
    #check if the home is close to work
    # citizen tax is applied 
    # from their salaty to the city budgetß
    # this will be applied from the residential class 
    