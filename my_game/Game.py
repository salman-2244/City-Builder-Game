# import tkinter as tk
# import pyautogui as paug
# from tkinter import *
# from tkinter import messagebox
import pygame as pg  # importing pygame as pg
from Field import Field
import sys
sys.path.append('./GUIGame')  # importing sys library
sys.path.append('./Zones')
from pygame.locals import *  # So I can use the diff modules.
from Dropdown import Dropdown
from Zone import Zone
from button import Button
from button import Button
from City import City
from menuBar import menuBar
import time
from datetime import datetime, timedelta, timedelta
# from inputBox import InputBox
from Zone import general, inudstrial, residential, service, Zone
import time
import pygame.freetype
import re
import random


class Game():  # initiating game class.

    def __init__(self, screen, clock):
        self.screen = screen  # setting screen object to screen
        self.clock = clock  # setting clock object
        self.field_size = 50  # size of each field
        self.font = pg.font.SysFont(None, 24)
        self.grid_rows = int(screen.get_height() / self.field_size)  # calculate rows (use later)
        self.zoneNo = 0
        self.City = City("New York City", 18, 50)
        self.grid_cols = int(screen.get_width() / self.field_size)  # calculate cols
        self.line_width = 1  # width of grid lines
        self.fields =  [] # array of field class.
        self.initializeFields()  # calling initializeFields function
        # self.addBackground() 
        # self.initialRoad()
        self.speed = 1
        self.numbers = 0
        self.selectedBuilding = ""
        self.zoneChosed = ""
        self.isSelectedBuilding = False;
        self.clicks = 0
        self.square_indices = []
        self.now = datetime.now()
        self.minutes = self.now.minute
        self.hour = self.now.hour
        self.date = self.now.date()
        self.seconds = 0

        
        
    def run(self):
        self.playing = True  # untill player is playing it will be true
        self.timer = 0  # starter for timer  
        self.addBackground()
        # self.initialRoad()
        # 
        # 
        # self.draw() # we will delete it later
        while self.playing:  # while player is playing
            event_list = pg.event.get()
            self.draw() # we will delete it later
            self.timer += 1
            # self.facTree()
            # self.checkExplosions()
            self.drawDD(event_list)   
            self.clock.tick(60)  # limiting the game loop to a maximum of 60 frames per second
            self.events(event_list)
            
            if self.date.day % 30 == 0:
                self.City.maintnanceFee() # deducting the maintnance fee from the bank every 3 min 
                self.City.employPeriodically()
                self.City.periodicalHappy()
                self.City.periodicalTax()
                self.City.taxMoney()
            
            self.checkZones()
            # self.City.moveInAndOut()
            
            if self.zoneChosed == "Comemrcial" or self.zoneChosed == "Industrial" or self.selectedBuilding == "Police" or self.selectedBuilding == "Hospital":
                self.City.checkResidentialConnection(self.fields)
            self.drawInfo(self.screen, 50)
            # self.update()
    
    
    
    
    
    # def show_explosion(self):
    #         images = []
    #         for num in range(1, 6):
    #             # img = pygame.image.load(f"my_game/Assets/img/exp{num}.png")
    #             img = pygame.transform.scale(img, (200, 200))
    #             images.append(img)
    #         index = 0
    #         counter = 0
    #         explosion_time = 6000
    #         start_time = pygame.time.get_ticks()
    #         x = random.randint(0, 900 - 100)
    #         y = random.randint(150, 600 - 100)
    #         while pygame.time.get_ticks() - start_time < explosion_time:

    #             self.clock.tick(60)
    #             self.draw()
    #             #update explosion animation
    #             counter += 1
    #             if counter >= 4:
    #                 counter = 0
    #                 index += 1
    #                 if index >= len(images):
    #                     break

    #             # draw current frame of explosion
    #             self.screen.blit(images[index], (x, y))
    #             pygame.display.update()
    
    
    
    # def checkExplosions(self):
    #     matcher = 69
    #     randu = random.randint(0, 2000)
    #     if randu == matcher:
    #         num = 0
    #         explosion_duration = 6000
    #         spawn_time = pygame.time.get_ticks()  # initialize timer
    #         explosion_end_time = spawn_time + explosion_duration  # calculate when explosions should stop
    #         while num < 5:
    #             current_time = pygame.time.get_ticks()
    #             if current_time - spawn_time > 1000 and current_time < explosion_end_time:
    #                 self.show_explosion()  # spawn explosion
    #                 spawn_time = current_time  # reset timer
    #                 print(num)
    #                 num+=1
            

        
    
    # very very useful for for testing purposes
    def pDetails(self, police_pos):
         for field in self.fields: # this will keep the fields updated
            if (field.rect.collidepoint(police_pos)):
                print("I am Printing the details of the clicked field")
                print(field.building)
                print(field.road)
                print(field.zone.typ)
                print(field.zone)
                
                
     # to demolish roads   
    def roadDel(self, police_pos):
            # You can add the bank logic here.
        for field in self.fields: # this will keep the fields updated
            if (field.road and field.rect.collidepoint(police_pos)):
                print("hi from delete Road")
                field.road = False
                field.color =  (86, 148, 70);
                pg.draw.rect(self.screen, field.color, field.rect)     
        
        # DO NOT DELETE
        
        
    def reclassify(self, police_pos):
        cnt = 0
        self.clikcs = 0
        # You can add the bank logic here.
        for field in self.fields: # this will keep the fields updated
            
            if (field.zone != "general" and field.rect.collidepoint(police_pos)):
                print("hi from reclassify")
                if field.zone.typ == "residential":
                    zonex = field.zone.x
                    zoney = field.zone.y
                    zoneNum = field.zone.num
                    field.building = ""
                    
                    self.City.bank += 100
                    self.City.population -= len(field.zone.residents)
                    classZone = general('gen', 100, (zonex*10)+zoney);classZone.width = 50; classZone.height = 50; classZone.x = zonex; classZone.y = zoney;
                    field.zone= classZone
                    self.City.changeZones(field.zone, classZone)
                if field.zone.typ == "general":
                    zonex = field.zone.x
                    zoney = field.zone.y
                    field.building = ""
                    zoneNum = field.zone.num
                    del self.City.zones[cnt]
                    self.City.bank += 100
                    classZone = general('gen', 100, (zonex*10)+zoney);classZone.width = 50; classZone.height = 50; classZone.x = zonex; classZone.y = zoney;
                    field.zone= classZone
                    self.City.changeZones(field.zone, classZone)
                if field.zone.typ == "service":
                    zonex = field.zone.x
                    field.building = ""
                    zoney = field.zone.y
                    zoneNum = field.zone.num
                    del self.City.zones[cnt]
                    self.City.bank += 100
                    classZone = general('gen', 100, (zonex*10)+zoney);classZone.width = 50; classZone.height = 50; classZone.x = zonex; classZone.y = zoney;
                    field.zone= classZone
                    self.City.changeZones(field.zone, classZone)
                if field.zone.typ == "industrial":
                    zonex = field.zone.x
                    zoney = field.zone.y
                    field.building = ""
                    zoneNum = field.zone.num
                    del self.City.zones[cnt]
                    self.City.bank += 100
                    classZone = general('gen', 100, (zonex*10)+zoney);classZone.width = 50; classZone.height = 50; classZone.x = zonex; classZone.y = zoney;
                    field.zone= classZone        
                    self.City.changeZones(field.zone, classZone)    
                pg.draw.rect(self.screen, field.color, field.rect) 
                        
                    
                    
        #         
    def removeBigImg(self, pos):
        building = "abc"         
        self.clicks += 1                                                                
        for i, fld in enumerate(self.fields):
            if (fld.rect.collidepoint(pos) and fld.building != "" ) or (fld.road == True and fld.rect.collidepoint(pos)):
                # Remove the stadium image from the screen
                building = fld.building 
                if fld.road == True: #and pos[0] in range (field.x, field.x + 50) and pos[1] in range (field.y, field.y + 50):
                        # print(field.x , field.y)
                        print(f"is destructible {fld.destructible(self.fields)}")
                        if fld.destructible(self.fields) != False:
                            print("I am inside road to destroy")
                            # field.road = False
                            fld.zone.road = False
                            for road in self.City.roads:
                                if road.x == fld.x and road.y == fld.y:
                                    self.City.roads.remove(road)
                                    fld.color = (86, 148, 70);
                                    print("I removed the road")
                                    
                                    #break
                            # break
                        else: 
                            print("Undestructible road")
                        fld.building = ""
                # print(building)
                else:
                    for field in self.fields: # this will keep the fields updated
                        #(field.building.startswith("stadium") or field.building.startswith("police"))
                        if (field.zone.typ == "general" and  field.building == building):
                            field.zone.police = False
                            field.zone.stadium = False
                            if field.building.startswith("stadium") and self.City.StadCnt > 0:
                                self.City.StadCnt -= 1
                            elif field.building.startswith("police") and self.City.polCnt > 0:
                                self.City.polCnt -= 1
                            # print(field.building)
                            # print(building)
                            field.building = ""
        
    
    # Set images on one field.
    def setImg(self, police_pos, img, option):
        police_img = pg.image.load(img)
        newSize = (50, 50)
        scaled_image = pg.transform.scale(police_img, newSize)
        print(police_pos)
        for i, fld in enumerate(self.fields):
            if fld.rect.collidepoint(police_pos) and fld.building == "" and fld.road == False:
                fld.building = option;
                police_rect = scaled_image.get_rect()
                police_rect.center = fld.rect.center
                self.screen.blit(scaled_image, police_rect)
                # Draw border around the field
                border_rect = pg.Rect(fld.rect.topleft, (self.field_size, self.field_size))
                pg.draw.rect(self.screen, (255, 0, 0), border_rect, 3)
                

        pg.display.flip()
        self.selectedBuilding = ""
        self.clicks = 0
    

    def drawZone(self, police_pos, img, zone):
        police_img = pg.image.load(img)
        newSize = (50, 50)
        self.zoneChosed = ""
        scaled_image = pg.transform.scale(police_img, newSize)
        print(police_pos)
        for i, fld in enumerate(self.fields):
            if fld.rect.collidepoint(police_pos) and fld.building == "" and fld.road == False:
                print("preparing")
                fld.building = img;
                # fld.zone = zone
                police_rect = scaled_image.get_rect()
                police_rect.center = fld.rect.center
                self.screen.blit(scaled_image, police_rect)
                # Draw border around the field
                border_rect = pg.Rect(fld.rect.topleft, (self.field_size, self.field_size))
                pg.draw.rect(self.screen, (255, 0, 0), border_rect, 3)
                if zone == "Residential":
                    # print("drawn")
                    classZone = residential(zone, 100, (fld.x*10)+fld.y)
                    classZone.x = fld.x; classZone.y = fld.y; classZone.width = 50; classZone.height = 50;
                    city = self.City
                    classZone.createInitialResidents(self.City); 
                    classZone.deductPrice(self.City)
                    classZone.accesible = classZone.isRoad(city);
                    fld.zone = classZone
                    self.City.zones.append(fld.zone)
                    print(self.City.population)
                    # classZone.deductPrice(self.City)
                    print(f"class zone x and y {classZone.x} and {classZone.y} is road {classZone.accesible}")
                    
                    fld.zone = classZone
                if zone == "service":
                    classZone = service(zone, 100, (fld.x*10)+fld.y)
                    classZone.x = fld.x; classZone.y = fld.y; classZone.width = 50; classZone.height = 50;
                    city = self.City
                    print(f"Roads size {len(self.City.roads)}")
                    classZone.accesible = classZone.isRoad(city);
                    classZone.addWorkers(self.City)
                    fld.zone = classZone
                    self.City.zones.append(fld.zone)
                    # classZone.deductPrice(self.City)
                    print(f"class zone x and y {classZone.x} and {classZone.y} is road {classZone.accesible}")
                if zone == "inudstrial":
                    classZone = inudstrial(zone, 100, (fld.x*10)+fld.y)
                    classZone.x = fld.x; classZone.y = fld.y; classZone.width = 50; classZone.height = 50;
                    city = self.City
                    print(f"Roads size {len(self.City.roads)}")
                    classZone.accesible = classZone.isRoad(city);
                    classZone.satsifaction(self.City)
                    classZone.addWorkers(self.City)
                    fld.zone = classZone
                    self.City.zones.append(fld.zone)
                    # classZone.deductPrice(self.City)
                    print(f"class zone x and y {classZone.x} and {classZone.y} is road {classZone.accesible}")
            
                    fld.zone = classZone
                pg.display.flip()

    
    def facTree(self):
        for i, fld in enumerate(self.fields):
                if i == 2:  
                    self.setImg((130,150), "my_game/Assets/tree.png", "forest")
                if i == 22:
                    self.setImg((130,200), "my_game/Assets/tree.png", "forest")
                if i == 3:  
                    self.setImg((180,150), "my_game/Assets/tree.png", "forest")
                if i == 23:
                    self.setImg((180,200), "my_game/Assets/tree.png", "forest")
                if i == 40:
                    self.setImg((810,400), "my_game/Assets/tree.png", "forest")
                if i == 41:
                    self.setImg((810,460), "my_game/Assets/tree.png", "forest")
                if i == 42:
                        self.setImg((860,400), "my_game/Assets/tree.png", "forest")
                if i == 43:
                    self.setImg((860,460), "my_game/Assets/tree.png", "forest")
                     
                    
                    
                

    def checkZones(self):
        for z in self.City.zones:
            if z.isRoad(self.City):
                z.accesible = True

    def currentTime(self, speed):
       
        
        if speed == 1:
                self.seconds += 1
                if self.seconds >= 60:
                    self.minutes += 1
                    self.seconds = 0
                    if(self.minutes == 60):
                        self.hour += 1
                        self.minutes = 0
                        self.seconds = 0
                        if(self.hour == 24):
                            self.hour = 0
                            self.minutes = 0
                            self.seconds = 0
                            self.date += timedelta(days=1)
                            # print(f"{hour}:{minutes}:{seconds}")
        if speed == 2:
                self.seconds += 2
                if self.seconds >= 60:
                    self.minutes += 1
                    self.seconds = 0
                    if(self.minutes == 60):
                        self.hour += 1
                        self.minutes = 0
                        self.seconds = 0
                        if(self.hour == 24):
                            self.hour = 0
                            self.minutes = 0
                            self.seconds = 0
                            self.date += timedelta(days=1)
                            # print(f"{hour}:{minutes}:{seconds}")
        if speed == 3:
                self.seconds += 50
                if self.seconds >= 60:
                    self.minutes += 1
                    self.seconds = 0
                    if(self.minutes == 60):
                        self.hour += 1
                        self.minutes = 0
                        self.seconds = 0
                        if(self.hour == 24):
                            self.hour = 0
                            self.minutes = 0
                            self.seconds = 0
                            self.date += timedelta(days=1)
        return(f"{self.date} {self.hour}:{self.minutes}:{self.seconds}")
     
     
    def drawInfo(self, screen, value ):  
        info = []
        hapiness = 0
        cnt = 0
        if self.City.population > 0:
            happiness = self.City.happiness
            for zone in self.City.zones:
                if zone.name == "res":
                    cnt += 1
                    happiness += zone.getHapiness()
                if cnt > 0:
                    happiness = happiness / cnt
        else:
            happiness = 50
        if happiness > 100:
            happiness = 100
            
             # --------------------- Info ---------------------------------------
        time = self.currentTime(1)
        info = [self.City.name, self.City.population, self.City.bank, time,happiness]
        font = pygame.freetype.SysFont("Arial", 20)
        # mb = menuBar(self.screen, 0, 40, screen.get_width(), 60, info)# creating a menu bar object
        # mb.displayItems(screen, info, (255,255,255) )
        # color = (0,0,204)
        # pg.draw.rect(screen, color, pg.Rect(0, 40, screen.get_width(),60))
        # # pg.display.update()
        
        # mb.displayItems(screen, info, (255,255,255) ) # drawing the menu bars
        
        score = self.font.render(f"Date: {time} Population: {self.City.population} Satisfaction: {self.City.happiness}, Bank: {round(self.City.bank)}$",True ,(255, 255, 255))
        txt_rect = score.get_rect(x = 10, y = 55)
        pg.draw.rect(self.screen, (26,108,172), txt_rect)

        screen.blit(score, txt_rect)
        
        # print("Happiness is, ",happiness )
        # print("Population is, ",self.City.population)
        # print("Bank is, ",self.City.bank )
    
    
    
    
    # Set images on 2x2 fields.
    def setBigImg(self, police_pos, img, option):
        # Get the indices of the fields in the 2x2 square
        self.numbers+=1
        temp = True
        square_indices = []
        for i, fld in enumerate(self.fields):
            if fld.rect.collidepoint(police_pos) and fld.road == False and fld.building == "":
                if (i % self.grid_cols < self.grid_cols - 1) and (i // self.grid_cols < self.grid_rows - 1):
                    if fld.building != "":
                        print("Cannot overlap ")
                        pg.display.update()
                        break
                        
                    square_indices.extend([i, i+1, i+self.grid_cols, i+self.grid_cols+1])
                   
                    # for g in self.square_indices:
                    #     print(g)
                    break
        for i, fld in enumerate(self.fields):
                if i in square_indices and fld.road:
                    temp = False
                    break;
    # Draw a border around the fields in the 2x2 square
        if square_indices and temp:
            top_left = self.fields[square_indices[0]].rect.topleft
            bottom_right = self.fields[square_indices[-1]].rect.bottomright
            border_rect = pg.Rect(top_left, (bottom_right[0]-top_left[0], bottom_right[1]-top_left[1]))
            pg.draw.rect(self.screen, (250, 100, 100), border_rect, 2)
            police_img = pg.image.load(img)
            scaled_image = pg.transform.scale(police_img, (self.field_size*2, self.field_size*2))
            image_rect = scaled_image.get_rect(center=border_rect.center)
            self.screen.blit(scaled_image, image_rect)
            self.selectedBuilding = ""

            for i, fld in enumerate(self.fields):
                if i in square_indices:
                    fld.building = option + str(self.numbers)
                    if option == "police":
                        print("Adding police to sat")
                        fld.zone.police = True
                        fld.zone.addWorkers(self.City)
                        fld.zone.satsifaction(self.City)
                    elif option == "stadium":
                        fld.zone.stadium = True
                        fld.zone.addWorkers(self.City)
                        fld.zone.satsifaction(self.City)
                        
                    print(fld.building);       
        if option == "police":
            self.City.polCnt += 1
            

        elif option == "stadium":
            self.City.StadCnt += 1
            
        pg.display.flip()



    
    # set the Road
    def setRoad(self, police_pos):
        cnt=0;
        print(police_pos)
        for i, fld in enumerate(self.fields):
            if fld.rect.collidepoint(police_pos):
                fld.color = (65, 65, 65)
                fld.road = True;
                cnt += 1
                zone = general("general",0, cnt)
                zone.x = fld.x
                zone.y = fld.y
                zone.width = 50
                zone.height = 50
                zone.road = True
                self.City.bank -= 3
                self.City.roads.append(zone)
                fld.zone = zone
        self.selectedBuilding = ""
        # pg.display.flip()
        # self.update()   
        
        

    

            
            

    def initializeFields(self):  # initialize the fields, adding them to fields array
         for row in range(2, self.grid_rows): # starting from 3rd row as first 3 rows are for menu
            for col in range(self.grid_cols):
                x = col * self.field_size
                y = row * self.field_size
                fld = Field(x, y, self.field_size)
                fld.grid_pos = (row, col)
                zone = general("general",0, 0)
                zone.x = fld.x
                zone.y = fld.y
                fld.zone = zone
                fld.id = (row*10)+col
                zone.width = 50
                zone.height = 50
                self.fields.append(fld)
                
                

    def initialRoad(self):
        cnt = 0
        # Change the color of fields in the middle to grey
        for fld in self.fields:
            cnt+=1;
            row, col = fld.grid_pos
            if row == (self.grid_rows) // 2 or col == (self.grid_cols) // 2:
                fld.color = (65, 65, 65)  # set color to grey for middle field
                fld.road = True;
                # print("inside initial road")
                # Comment for Clearity
                
                zone = general("general",0, cnt)
                zone.road = True
                fld.zone = zone
                zone.x = fld.x
                zone.y = fld.y
                zone.width = 50
                zone.height = 50
                zone.road = True
                self.City.zones.append(zone)
                self.City.roads.append(zone)
        self.update()
                

    def events(self, event_list):
        
        for event in event_list: # getting all events
            if event.type == pg.QUIT: # if player click exit then exit
                self.playing = False;
                pg.quit();
                sys.exit()
            elif event.type == pg.KEYDOWN:  # if key is pressed
                if event.key == pg.K_ESCAPE: # if player press esc key then exit
                     self.playing = False;
                     pg.quit();
                     sys.exit();
            elif event.type == pg.MOUSEBUTTONDOWN:
             
               
                      police_pos = event.pos
                      print(police_pos);
                      if event.button == 1:  # if left mouse button is press
                            
                            self.clicks +=1;
                            print("from events menu")
                            # self.pDetails(police_pos)

                            print(self.clicks)
                            if (self.selectedBuilding != "" and self.clicks == 2):
                                if (self.selectedBuilding == "police"):
                                    print("Inside  police events")
                                    self.setBigImg(police_pos, "my_game/Assets/police.png", "police")
                                elif(self.selectedBuilding == "road"): 
                                    self.setRoad(police_pos)
                                elif(self.selectedBuilding == "stadium"):
                                    self.setBigImg(police_pos, "my_game/Assets/stadium.png", "stadium")
                                elif (self.selectedBuilding == "forest"):
                                    self.setImg(police_pos, "my_game/Assets/tree.png", "forest")
                                elif (self.selectedBuilding == "reclassify"):
                                    self.reclassify(police_pos)
                                elif (self.selectedBuilding == "demolish"):
                                    # for field in self.fields:
                                    #     print((field.zone.typ))
                                        # print((field.building))
                                    self.removeBigImg(police_pos)
                                
                            
                            if(self.zoneChosed != "" and self.clicks == 2):
                                if(self.zoneChosed == "Residential"):
                                    self.drawZone(police_pos, "my_game/Assets/house.png", "Residential")
                                elif(self.zoneChosed == "Commercial"):
                                    self.drawZone(police_pos, "my_game/Assets/police.png", "service")
                                elif(self.zoneChosed == "Industrial"):
                                    self.drawZone(police_pos, "my_game/Assets/factory.png", "inudstrial")
                                else:
                                    print("No zone choosed") 
                                self.update()
                        
        #             self.dragging = True
                   
        #     elif event.type == pg.MOUSEBUTTONUP:
        #         if event.button == 1:  # if left mouse button is released
        #             self.dragging = False
        #     elif event.type == pg.MOUSEMOTION:
        #         if self.dragging:  # if left mouse button is held down and mouse is moving

        #             for field in self.fields:
        #                 if field.rect.collidepoint(event.pos):
                            
        #                     if not field.selected:
        #                     # mark the field as selected and change its color
        #                         field.selected = True
        #                         # field.color = (0, 140, 120)
        # # create a border around the selected field
        #                     # if field.selected:
        #                     #     field_border = pg.Rect(field.rect.x - 2, field.rect.y - 2, field.rect.width + 4, field.rect.height + 4)
        #                     #     pg.draw.rect(self.screen, (0, 0, 255), field_border, 8)
                                


                    

   
                                  
    #and field.zone != None
    def update(self):
        for field in self.fields: # this will keep the fields updated
            # and  field.zone.typ == "general"
            if (field.building == "" and  field.zone.typ == "general"):
                pg.draw.rect(self.screen, field.color, field.rect)
        self.drawGrid()
        # pg.display.flip()

    # addition of the bacground image
    def addBackground(self):
        bg = pg.image.load("/Users/markoboreta/Desktop/other/my_game/Assets/bg1.jpg")
        bg = pg.transform.scale(bg, (900, 600))
        self.screen.blit(bg, (0, 0))

    def drawGrid(self):
        for x in range(0, self.screen.get_width(), self.field_size):  # drawing vertical lines
            pg.draw.line(self.screen, (255, 255, 255), (x, 100), (x, self.screen.get_height()),1)
        for y in range(100, self.screen.get_height(), self.field_size):  # drawing horizonal lines
            pg.draw.line(self.screen, (255, 255, 255), (0, y), (self.screen.get_width(), y),1)
            
            
    def draw(self):
        self.initialRoad()
        self.drawGrid()
        pg.display.flip()
        
      

    
    
    def drawDD(self, event_list):
                # --------------------- Zones list ---------------------------------------
        image = pg.image.load("./GUIGame/Buttons/zones.png")
        imgSize = (image.get_width(), image.get_height())    
        # # creating button instancess 
        ini = pg.image.load("./GUIGame/Buttons/General.png");ini = pg.transform.scale(ini, imgSize)
        general = Button(0, 0, ini, 1);general.setText("General")
        comm = pg.image.load("./GUIGame/Buttons/Commercial.png");comm = pg.transform.scale(comm, imgSize)
        commercial = Button(0, 0, comm, 1);commercial.setText("Commercial")
        ind = pg.image.load("./GUIGame/Buttons/industrial.png");ind = pg.transform.scale(ind, imgSize)
        industrial = Button(0, 0, ind, 1);industrial.setText("Industrial")
        res = pg.image.load("./GUIGame/Buttons/Res.png");res = pg.transform.scale(res, imgSize)
        residential = Button(0, 0, res, 1);residential.setText("Residential")
        
        # for the zone dropdown menu
        list1 = Dropdown(pg.font.SysFont(None, 30),700, 0, 50, 30,"Zones", [commercial, industrial, residential], image)
        selected_option = list1.updateDD(event_list)
        if selected_option >= 0:
            if selected_option == 0:
                print("General")
                # pyautogui.prompt(text='', title='Enter Amout of Tax' , default='')
                # self.selectedBuilding = "reclassify"
                self.zoneChosed = "Commercial"
                # pyautogui.alert(" Commercial Zone is Selected")
                self.clicks =0;
                
                # COMMENT THIS PART IF YOU DO NOT WANT TO DO EXPLOSIONS 
                # num = 0
                # explosion_duration = 6000
                # spawn_time = pygame.time.get_ticks()  # initialize timer
                # explosion_end_time = spawn_time + explosion_duration  # calculate when explosions should stop
                # while num < 5:
                #     current_time = pygame.time.get_ticks()
                #     if current_time - spawn_time > 1000 and current_time < explosion_end_time:
                #         self.show_explosion()  # spawn explosion
                #         spawn_time = current_time  # reset timer
                #         print(num)
                #         num+=1

                
            elif selected_option == 1:
                self.zoneChosed = "Industrial"
                # pyautogui.alert(" Industrial Zone is Selected")
                self.clicks =0;
            elif selected_option == 2:
            #    pyautogui.alert(" Residential Zone is Selected")
               self.zoneChosed = "Residential"
               print("Residential")
               self.clicks =0;
            else:
                print("No option selected")
            list1.main = list1.options[selected_option]
        s1 = selected_option
        list1.drawDD(self.screen)
        # spriteGroup = pg.sprite.Group()        
        # ------------------------------- Build list -------------------------------------
        forest = pg.image.load("./GUIGame/Buttons/Forest.png");forest = pg.transform.scale(forest, imgSize)
        forBut = Button(0, 0, forest, 1);forBut.setText("Forest")
        pol = pg.image.load("./GUIGame/Buttons/police.png");pol = pg.transform.scale(pol, imgSize)
        police = Button(0, 0, pol, 1);police.setText("Police")
        stad = pg.image.load("./GUIGame/Buttons/stad.png");stad = pg.transform.scale(stad, imgSize)
        stadium = Button(0, 0, stad, 1);stadium.setText("Stadium")
        road = pg.image.load("./GUIGame/Buttons/road.png");road = pg.transform.scale(road, imgSize)
        roadBut = Button(0, 0, road, 1);roadBut.setText("Road")
        image_build = pg.image.load("./GUIGame/Buttons/build.png")
        list2 = Dropdown(pg.font.SysFont(None, 30), 600, 0, 50, 30, "Build",
                               [police, stadium, roadBut, forBut], image_build)
        selected_option2 = list2.updateDD(event_list)
        # print(selected_option2);
        
        if selected_option2 >= 0:
            if selected_option2 == 0:  
                # pyautogui.alert("Police is Selected")
                self.selectedBuilding = "police"
                self.clicks =0;
                # pyautogui.prompt(text='', title='Enter Amout of Tax' , default='')

            elif selected_option2 == 1:
                # pyautogui.alert(" Stadium is Selected")
                self.selectedBuilding = "stadium"
                self.clicks = 0
            elif selected_option2 == 2:
            #    pyautogui.alert(" Road is Selected")
               self.selectedBuilding = "road"
               self.clicks = 0
            elif selected_option2 == 3:
                # pyautogui.alert(" Forest is Selected")
                self.selectedBuilding = "forest"
                self.clicks =0;
            else:
                print("No option selected")
            list2.main = list2.options[selected_option2]
        list2.drawDD(self.screen)
        
        buttImg = pg.image.load("/Users/markoboreta/Desktop/other/GUIGame/Buttons/other.png")
        buttImg =  pg.transform.scale(buttImg, imgSize)
        # imgSize = (image.get_width(), image.get_height())    
        # # # creating button instancess 
        dem = pg.image.load("/Users/markoboreta/Desktop/other/GUIGame/Buttons/demolish.png");dem = pg.transform.scale(dem, imgSize)
        demolsih = Button(0, 0, dem, 1);demolsih.setText("demolish")
        reclas = pg.image.load("/Users/markoboreta/Desktop/other/GUIGame/Buttons/reclass.png");reclas = pg.transform.scale(reclas, imgSize)
        reclass = Button(0, 0, reclas, 1);reclass.setText("reclass")
        # ind = pg.image.load("./GUIGame/Buttons/industrial.png");ind = pg.transform.scale(ind, imgSize)
        # industrial = Button(0, 0, ind, 1);industrial.setText("Industrial")
        # res = pg.image.load("./GUIGame/Buttons/Res.png");res = pg.transform.scale(res, imgSize)
        # residential = Button(0, 0, res, 1);residential.setText("Residential")
        
        list3 = Dropdown(pg.font.SysFont(None, 30), 800, 0, 50, 30, "Other", [demolsih, reclass], buttImg)
        selected_option3 = list3.updateDD(event_list)
        # print(selected_option2);
        
        if selected_option3 >= 0:
            if selected_option3 == 0:
                print("Demolish")
                # pyautogui.prompt(text='', title='Enter Amout of Tax' , default='')
                # self.selectedBuilding = "reclassify"
                self.selectedBuilding = "demolish"
                self.clicks =0
                # pyautogui.prompt(text='', title='Enter Amout of Tax' , default='
            elif selected_option3 == 1:
                print("Reclassify")
                # pyautogui.alert(" Stadium is Selected")
                self.selectedBuilding = "reclassify"
                self.clicks = 0
            # elif selected_option2 == 2:
            # #    pyautogui.alert(" Road is Selected")
            #    self.selectedBuilding = "road"
            #    self.clicks = 0
            # elif selected_option2 == 3:
            #     # pyautogui.alert(" Forest is Selected")
            #     self.selectedBuilding = "forest"
            #     self.clicks =0;
            else:
                print("No option selected")
            list3.main = list3.options[selected_option2]
        list3.drawDD(self.screen)
        
        pg.display.flip()
        
        
    # Explosion Class
    ##############################################################
    
    
    


    
        
    # Some Other functions that can be used later
    #####################################################################################################
        
    #     def mess(self):
    #         # Initialize Pygame
    #         pg.init()

    #     # Create a new Pygame display for the message box
    #     message_width = 320
    #     message_height = 240
    #     message_screen = pg.display.set_mode((message_width, message_height))
    #     pg.display.set_caption("Message Box")

    #     # Show the message box using the tkinter messagebox module
    #     messagebox.showinfo("Title", "This is a message box.")

    #     # Clear the message screen and update the display
    #     message_screen.fill((0, 0, 0))
    #     pg.display.update()

    #     # Wait for the user to dismiss the message box
    #     running = True
    #     while running:
    #         for event in pg.event.get():
    #             if event.type == pg.QUIT:
    #                 running = False

    #     # Close the Pygame display for the message box
    #     pg.quit()
    
    # def setCursor(self,img):
        
    #     pg.mouse.set_visible(False)
    #     police_img = pg.image.load(img).convert_alpha()
    #     newSize = (50,50)
    #     scaled_image = pg.transform.scale(police_img, newSize)
    #     self.cursor_img = scaled_image

    
    
    
    #  def selection(self, event_list):
    #         for event in event_list:
    #         if event.button == 1:  # if left mouse button is pressed
    #                 self.dragging = True
                   
    #         elif event.type == pg.MOUSEBUTTONUP:
    #             if event.button == 1:  # if left mouse button is released
    #                 self.dragging = False
    #         elif event.type == pg.MOUSEMOTION:
    #             if self.dragging:  # if left mouse button is held down and mouse is moving

    #                 for field in self.fields:
    #                     if field.rect.collidepoint(event.pos):
                            
    #                         if not field.selected:
    #                         # mark the field as selected and change its color
    #                             field.selected = True
    #                             # field.color = (0, 140, 120)
    #     # create a border around the selected field
    #                         # if field.selected:
    #                         #     field_border = pg.Rect(field.rect.x - 2, field.rect.y - 2, field.rect.width + 4, field.rect.height + 4)
    #                         #     pg.draw.rect(self.screen, (0, 0, 255), field_border, 8)  


###################### BORDERS ###############################


     # for field in self.fields: # this will keep the fields updated
        #     if field.selected and field.road == False:
        #     # pg.draw.rect(self.screen, field.color, field.rect)
        #         field_border = pg.Rect(field.rect.x - 2, field.rect.y - 2, field.rect.width + 4, field.rect.height + 4)
        #         pg.draw.rect(self.screen, (250, 100, 100), field_border, 2)
        
        # print("dfj")







