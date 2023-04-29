import pygame as pg 
import sys  # importing sys library
from my_game.Game import Game
from my_game.Field import Field
from Zones.zone import zone

class World:
    def __init__(self):
        self.Fields = []
        self.Zones = []
        self.Roads = []
        self.Name = "New York City"
        self.Bank = 200000 # initial budget of the city
        self.Citizens = 0
        self.citizen_tax = 18 # in percentage
        self.citizen_happiness = 0 # in pertentage

    
    def check_road(self, x, y): # checking if there is a road on the field
        field = self.get_field(x, y)
        if field is not None:
            return field.road
        return False # if there is no road on the field
    
    def get_zones(self):
        return self.Zones
    
    def addUpCitizen(self): # number of citizens
        for i in range(self.Zones): 
            self.Citizens += i.getResidents()
    def get_citizens(self):
        return self.Citizens
    
    def buy(self, amount):
        self.Bank -= amount
    
    def collectTax(self): # collecting the tax from the citizens
        for i in self.Zones:
            if i.getName() == "Residential":
                for r in i.getResidents(): # iterate over the zones and over the residatial zone dictionary
                    if r["job"] == "office":
                        self.Bank += 1000 * self.citizen_tax
                    else:
                        self.Bank += 850 * self.citizen_tax
    def get_bank(self):
        return self.Bank
    
    



        
    