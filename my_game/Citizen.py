

# Citizen class

class Citizen(): 
    def __init__(self, id, workZone, salary, happy, home):
        self.id = id
        self.workZone = workZone
        self.salary = salary
        self.happy = happy
        self.home = home
            # self.work = work
    
    def toDict(self):
        return {"id": self.id, "workZone": self.workZone, "salary": self.salary, "happy": self.happy, "home": self.home}
    
    