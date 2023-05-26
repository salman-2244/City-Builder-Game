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
        """_summary_

        Args:
            salary (int): Salary of the citizen
            tax (Int): tax applied to the salary
            distance (Int): distance from home to work

        Returns:
            _percentage of happiness
        """
        self.happy = (salary - (salary * (tax/100))) - (distance * 0.1)
        if distance == 0: # unemployed
            self.happy = 0
        if self.happy < 0: 
            self.happy = 0
        return self.happy
    