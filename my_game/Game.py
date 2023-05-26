import tkinter as tk
import pyautogui as paug
from tkinter import *
import pygame as pg  # importing pygame as pg
from Field import Field
import sys
sys.path.append('./GUIGame')  # importing sys library
sys.path.append('./Zones')
sys.path.append('./Buildings')
from pygame.locals import *  # So I can use the diff modules.
from Dropdown import Dropdown
# from Zones import zone
from button import Button
from button import Button
from City import City
import time
from datetime import datetime, timedelta, timedelta
# from inputBox import InputBox
from zone import general, industrial, residential, service, Zone
from Buildings import Forest
import time
import pygame.freetype
import random


class Game():  # initiating game class.

    def __init__(self, screen, clock):
        self.screen = screen  # setting screen object to screen
        self.clock = clock  # setting clock object
        self.field_size = 50  # size of each field
        self.font = pg.font.SysFont(None, 20)
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
        self.image_rect = None
        

        
        """_summary_
            This function is used to run the game while the player is playing.
            """   
    def run(self):
        """
        This function is used to run the game while the player is playing.
        """
        self.playing = True  # untill player is playing it will be true
        self.timer = 0  # starter for timer  
        self.addBackground()
        # self.initialRoad()
        # 
        # self.facTree()
        # self.draw() # we will delete it later
        # self.update()
        
        while self.playing:  # while player is playing
            event_list = pg.event.get()
            # we will delete it later
            self.timer += 1
            
            # self.checkExplosions()
            self.draw()
            self.renderSmallImg()
            self.renderBigImages()
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
            if self.timer % 300 == 0:
                self.City.moveInAndOut()
            
            if self.zoneChosed == "Comemrcial" or self.zoneChosed == "Industrial" or self.selectedBuilding == "Police" or self.selectedBuilding == "Hospital":
                self.City.checkResidentialConnection(self.fields)
            self.drawInfo(self.screen, 50)
            
            # self.update()
            if self.City.happiness == 0:
                self.playing = False
                # self.gameOver()
    
    
    
    
    
    def renderBigImages(self):
        for fld in self.fields:
            if fld.image_rect is not None:
                pg.draw.rect(self.screen, fld.color, fld.rect)
                self.screen.blit(fld.Bimg, fld.image_rect)
                # Draw border around the field
                border_rect = pg.Rect(fld.rect.topleft, (self.field_size, self.field_size))
                pg.draw.rect(self.screen, (255, 0, 0), fld.image_rect, 2)
        # Other rendering code goes here
        # pg.display.flip()
        
        
    def renderSmallImg(self):
        for fld in self.fields:
            # 
             if fld.img is not None  :
                pg.draw.rect(self.screen, fld.color, fld.rect)
                self.screen.blit(fld.img, fld.rect)
                # # Draw border around the field
                border_rect = pg.Rect(fld.rect.topleft, (self.field_size, self.field_size))
                pg.draw.rect(self.screen, (255, 0, 0), border_rect, 2)
        # Other rendering code goes here
        # pg.display.flip()
    
    def show_explosion(self):
            images = []
            for num in range(1, 6):
                img = pg.image.load(f"my_game/Assets/img/exp{num}.png")
                img = pg.transform.scale(img, (200, 200))
                images.append(img)
            index = 0
            counter = 0
            explosion_time = 6000
            start_time = pg.time.get_ticks()
            x = random.randint(0, 900 - 100)
            y = random.randint(150, 600 - 100)
            while pg.time.get_ticks() - start_time < explosion_time:

                self.clock.tick(60)
                self.draw()
                #update explosion animation
                counter += 1
                if counter >= 4:
                    counter = 0
                    index += 1
                    if index >= len(images):
                        break

                # draw current frame of explosion
                self.screen.blit(images[index], (x, y))
                pg.display.update()
    
    
    
    def checkExplosions(self):
        matcher = 69
        randu = random.randint(0, 5000)
        if randu == matcher:
            num = 0
            explosion_duration = 6000
            spawn_time = pg.time.get_ticks()  # initialize timer
            explosion_end_time = spawn_time + explosion_duration  # calculate when explosions should stop
            while num < 5:
                current_time = pg.time.get_ticks()
                if current_time - spawn_time > 1000 and current_time < explosion_end_time:
                    self.show_explosion()  # spawn explosion
                    spawn_time = current_time  # reset timer
                    print(num)
                    num+=1
        
    
    # very very useful for for testing purposes
        """
        _summary_
        
        """    
    # def pDetails(self, police_pos):
    #     """

    #     Args:
    #         police_pos (tuple of int): tuple of x and y coordinates of the mouse click
    #         clicked field details are printed on the console
    #     """
    #     for field in self.fields: # this will keep the fields updated
    #         if (field.rect.collidepoint(police_pos)):
    #             print("I am Printing the details of the clicked field")
    #             print(field.building)
    #             print(field.road)
    #             print(field.zone.typ)
    #             print(field.zone)
                
                
     # to demolish roads   
    def roadDel(self, police_pos):
        """
        _summary_
        This function is used to delete the roads.

        Args:
            police_pos (tuple): tuple of x and y coordinates of the mouse click
        """
            # You can add the bank logic here.

        for fld in self.fields: # this will keep the fields updated
            if (fld.road and fld.rect.collidepoint(police_pos)):
                        print(f"is destructible {fld.destructible(self.fields)}")
                        if fld.destructible(self.fields) != False:
                            print("I am inside road to destroy")
                            # field.road = False
                            self.selectedBuilding = ""
                            
                            fld.building = ""
                            print(f"Roads len is {len(self.City.roads)}")
                            for road in self.City.roads:
                                if road.x == fld.x and road.y == fld.y:
                                    self.City.roads.remove(road)
                                    fld.zone.road = False
                                    fld.color = (86, 148, 70);
                                
                                    print("I removed the road")
                                    print(f"the road is {fld.zone.road}")
                                    
                                    #break
                            # break
                        else: 
                            print("Undestructible road")
        # self.building = ""
         
        
        # DO NOT DELETE
        
    def instZone(self, x, y, typ, num):
        """
        Args :
            x (int): x coordinate of the mouse click
            y (int): y coordinate of the mouse click
            typ (str): type of the zone
            num (int): number of the zone
        Returns:
            zone (object): returns the zone object
        This function is used to instantiate the zone object.
        """
        zone = general(typ, num, (x*10)+y)
        if typ == "residential":
            zone = general(typ, num, (x*10)+y);zone.width = 50; zone.height = 50; zone.x = x; zone.y = y;
        elif typ == "commercial":
            zone = general(typ, num, (x*10)+y);zone.width = 50; zone.height = 50; zone.x = x; zone.y = y;
        elif typ == "industrial":
            zone = general(typ, num, (x*10)+y);zone.width = 50; zone.height = 50; zone.x = x; zone.y = y;
        # zone = general(typ, num, (x*10)+y);zone.width = 50; zone.height = 50; zone.x = x; zone.y = y;
        return zone
    
    
    def disasterEvent(self):
        """_summary_
        This function is used to instantiate the disaster event
        """
        self.City.bank -= 100000
        self.City.happiness -= 20
        cnt = 0
        random = random.randint(0, len(self.City.zones))
    
    
    
    
    
    def reclassify(self, police_pos):
        # You can add the bank logic here.
        for field in self.fields: # this will keep the fields updated
            if (field.zone != general and field.rect.collidepoint(police_pos) and field.building == field.zone.typ):
                print(field.zone)
                print(field.zone.typ)
                print("hi from reclassify")
                zone = general("general",0, 0)
                field.zone = zone
                print(field.building)
                field.building = ""
                field.img = None
                pg.draw.rect(self.screen, field.color, field.rect) 
                        
                    
                    
        #         
    def removeBigImg(self, pos):
        """_summary_
        Args:
            pos (tuple): tuple of x and y coordinates of the mouse click
            Removes the big image from the screen, police, stadium etc
        """
        building = "abc"         
        # self.clicks += 1                                                                
        for i, fld in enumerate(self.fields):
            if (fld.rect.collidepoint(pos) and fld.building != "" ) or (fld.road == True and fld.rect.collidepoint(pos)):
                building = fld.building 
                if fld.road == True: #and pos[0] in range (field.x, field.x + 50) and pos[1] in range (field.y, field.y + 50):
                        self.roadDel(pos)
                        fld.building = ""
                # print(building)
                else:
                    for field in self.fields: # this will keep the fields updated
                        #(field.building.startswith("stadium") or field.building.startswith("police"))
                        if (field.zone.typ == "general" and  field.building == building):
                            field.building = ""
                            field.image_rect = None
                            field.zone.police = False
                            field.zone.stadium = False
                            if field.building.startswith("stadium") and self.City.StadCnt > 0:
                                self.City.StadCnt -= 1
                            elif field.building.startswith("police") and self.City.polCnt > 0:
                                self.City.polCnt -= 1
                            # print(field.building)
                            # print(building)
                            
        
    
    # Set images on one field.
    def setImg(self, police_pos, img, option):
        """_summary_
        Args:
            police_pos (tuple): tuple of x and y coordinates of the mouse click
            img (string): path to the image
            option (string): building name 
            Sets the image on the field, police, stadium etc
        """
        police_img = pg.image.load(img)
        newSize = (50, 50)
        scaled_image = pg.transform.scale(police_img, newSize)
        print(police_pos)
        for i, fld in enumerate(self.fields):
            if fld.rect.collidepoint(police_pos) and fld.building == "" and fld.road == False:
                fld.building = option;
                police_rect = scaled_image.get_rect()
                police_rect.center = fld.rect.center
                # self.screen.blit(scaled_image, police_rect)
                # Draw border around the field
                border_rect = pg.Rect(fld.rect.topleft, (self.field_size, self.field_size))
                pg.draw.rect(self.screen, (255, 0, 0), border_rect, 3)
                

        pg.display.flip()
        self.selectedBuilding = ""
        self.clicks = 0
    

    def spawnZone(self, zone, fld):
        """_summary_
        Args:
            zone (zone): zone object
            fld (fld): field object

        Returns:
            zone: zone object
            Spawns the zone on the field
        """
        classZone = None
        if zone == "Residential":
            classZone = residential(zone, 100, (fld.x*10)+fld.y)
            classZone.x = fld.x; classZone.y = fld.y; classZone.width = 50; classZone.height = 50;
            self.City.bank -= 200
            classZone.accesible = classZone.f(self.City);
            print(f"the zone is {classZone.accesible}")
        if zone == "Service":
            classZone = service(zone, 100, (fld.x*10)+fld.y)
            classZone.x = fld.x; classZone.y = fld.y; classZone.width = 50; classZone.height = 50;  classZone.accesible = classZone.isRoad(self.City);
            self.City.bank -= 200
            print(f"the zone is {classZone.accesible}")
            classZone.addWorkers(self.City)
            classZone.satsifaction(self.City)
        if zone == "Industrial":
            classZone = industrial(zone, 100, (fld.x*10)+fld.y)
            classZone.x = fld.x; classZone.y = fld.y; classZone.width = 50; classZone.height = 50;  classZone.accesible = classZone.isRoad(self.City);
            self.City.bank -= 200
            classZone.addWorkers(self.City)
            classZone.satsifaction(self.City)
        return classZone

    def drawZone(self, police_pos, img, zone):
        """_summary_
        Args:
            police_pos (_type_): _description_
            img (string): path to the image
            zone (zone): zone object
        """
        police_img = pg.image.load(img)
        newSize = (50, 50)
        self.zoneChosed = ""
        self.clicks = 0
        scaled_image = pg.transform.scale(police_img, newSize)
        print(police_pos)
        for i, fld in enumerate(self.fields):
            if fld.rect.collidepoint(police_pos) and fld.building == "" and fld.road == False:
                print("preparing")
                fld.building = img;
                fld.img = scaled_image
                police_rect = scaled_image.get_rect();police_rect.center = fld.rect.center;
                self.screen.blit(scaled_image, police_rect)
                border_rect = pg.Rect(fld.rect.topleft, (self.field_size, self.field_size))
                pg.draw.rect(self.screen, (255, 0, 0), border_rect, 3)
                print(zone)
                if fld.zone.typ == "general" and fld.zone.police == False and fld.zone.stadium == False and fld.zone.road == False:
                    if zone == "Residential":
                        classZone = self.spawnZone(zone, fld)
                        classZone.createInitialResidents(self.City); 
                        classZone.deductPrice(self.City)
                        fld.zone = classZone
                        self.City.zones.append(fld.zone)
                    if zone == "Service":
                        classZone = self.spawnZone(zone, fld)
                        fld.zone = classZone
                        self.City.zones.append(fld.zone)
                    if zone == "Industrial":
                        classZone = self.spawnZone(zone, fld)
                        fld.zone = classZone
                        self.City.zones.append(fld.zone)
                    pg.display.flip()

    
    def drawTree(self, police_pos):
        """_summary_

        Args:
            police_pos (tuple): tuple of the position of the mouse
            Spawns a tree on the field
        """
        cnt=0;
        print(police_pos)
        for i, fld in enumerate(self.fields):
            if fld.rect.collidepoint(police_pos):
                
                if fld.zone.typ == "general": 
                        self.setImg((fld.x+10,fld.y+10), "my_game/Assets/tree.png", "forest")
                        fld.zone.forest = True
                        forest = Forest((fld.x*10), self.date.year, fld.zone, self.City)
                        seenby = forest.seen_By(self.City)
                        print(f"seen by {seenby}")
                        self.City.happiness += seenby
                        self.City.forests.append(forest)
                        self.City.forestImpact(self.fields)
                        print(f"forest added {seenby}")
        
        self.selectedBuilding = ""
        
        
    def initTree(self,fld):
        """_summary_

        Args:
            fld (field): field object
            Spawns a tree on the field
        """
        if fld.zone.typ == "general": 
                        fld.zone.forest = True
                        forest = Forest((fld.x*10), self.date.year, fld.zone, self.City)
                        self.City.forests.append(forest)
                        print(f"forest added {forest}")
    
    
    def facTree(self):
        """
        Spawns trees on the map
        """
        for i, fld in enumerate(self.fields):
                if i == 2:  
                    self.setImg((130,150), "my_game/Assets/tree.png", "forest")
                    self.initTree(fld)
                if i == 22:
                    self.setImg((130,200), "my_game/Assets/tree.png", "forest")
                    self.initTree(fld)
                if i == 3:  
                    self.setImg((180,150), "my_game/Assets/tree.png", "forest")
                    self.initTree(fld)
                if i == 23:
                    self.setImg((180,200), "my_game/Assets/tree.png", "forest")
                    self.initTree(fld)
                if i == 40:
                    self.setImg((810,400), "my_game/Assets/tree.png", "forest")
                    self.initTree(fld)
                if i == 41:
                    self.setImg((810,460), "my_game/Assets/tree.png", "forest")
                    self.initTree(fld)
                if i == 42:
                        self.setImg((860,400), "my_game/Assets/tree.png", "forest")
                        self.initTree(fld)
                if i == 43:
                    self.setImg((860,460), "my_game/Assets/tree.png", "forest")
                    self.initTree(fld)
        self.update()
            
                     
                    
    def gameSpeed(self, increaseBy):
        """_summary_

        Args:
            increaseBy (integer): increase the speed of the game by the amount of seconds
            Increases the speed of the game in real time
        """
        self.seconds += increaseBy
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
                            if self.date.day > 30:
                                self.date += timedelta(months=1)
                                if self.date.month > 12:
                                    self.date += timedelta(years=1)
                                    self.City.maintainForests(int(self.date.year))
            
                

    def checkZones(self):
        pass
        # for z in self.City.zones:
        #     if z.isRoad(self.City):
        #         z.accesible = True

    def currentTime(self, speed):
        """_summary_
        Args:
            speed (Ineteger):In which speed the game is running
            Updates the time in the game
        """
        if speed == 1:
            self.gameSpeed(1)                
        if speed == 2:
            self.gameSpeed(2)
        if speed == 3:
            self.gameSpeed(5)
        return(f"{self.date} {self.hour}:{self.minutes}:{self.seconds}")
     
     
    def drawInfo(self, screen, value ):
        """_summary_

        Args:
            screen (SCREEN): The screen on which the info will be displayed
            value (String): The value that will be displayed
            Displays the info on the screen
        """
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
            self.City.happiness = 100
            
             # --------------------- Info ---------------------------------------
        time = self.currentTime(1)
        score = self.font.render(f"Date: {time} Population: {self.City.population} Satisfaction: {self.City.happiness}, Bank: {round(self.City.bank)}$",True ,(255, 255, 255))
        txt_rect = score.get_rect(x = 10, y = 55)
        pg.draw.rect(self.screen, ((30,144,255)), txt_rect)

        screen.blit(score, txt_rect)
    
    
    
    def overlap(self, police_pos, square_indices):
        """_summary_
        Args:
            police_pos (tuple): The position of the police station
            square_indices (list): The list of the indices of the squares
        Returns:
            list: The list of the indices of the squares
            Checks if the police station overlaps with another building
        """
        for i, fld in enumerate(self.fields):
            if fld.rect.collidepoint(police_pos) and fld.road == False and fld.building == "":
                if (i % self.grid_cols < self.grid_cols - 1) and (i // self.grid_cols < self.grid_rows - 1):
                    if fld.building != "":
                        print("Cannot overlap ")
                        pg.display.update()
                        break
                    square_indices.extend([i, i+1, i+self.grid_cols, i+self.grid_cols+1])
                    break
        return square_indices
    
    
    def drawBorder(self, police_pos, square_indices, img, temp,fld):
        """_summary_

        Args:
            police_pos (tuple): The position of the police station
            square_indices (list): The list of the indices of the squares
            img (String): The image of the police station
            temp (Boolean): If the police station is temporary
            fld (Field): The field on which the police station will be built

        Returns:
            image: The image of the police station
            Draws the border of the police station
        """
        if square_indices and temp:
            top_left = self.fields[square_indices[0]].rect.topleft
            bottom_right = self.fields[square_indices[-1]].rect.bottomright
            border_rect = pg.Rect(top_left, (bottom_right[0]-top_left[0], bottom_right[1]-top_left[1]))
            pg.draw.rect(self.screen, (250, 100, 100), border_rect, 2)
            police_img = pg.image.load(img)
            scaled_image = pg.transform.scale(police_img, (self.field_size*2, self.field_size*2))
            fld.image_rect = scaled_image.get_rect(center=fld.rect.center)
            self.selectedBuilding = ""
            big_image = pg.Surface((self.field_size*2, self.field_size*2))
            big_image.fill((86, 148, 70))
            big_image.blit(scaled_image, (0, 0))
            return big_image, top_left        
    
    
    # Set images on 2x2 fields.
    # def setBigImg(self, police_pos, img, option):
    #     """_summary_
    #     Args:
    #         police_pos (tuple): The position of the police station
    #         img (String): The image that will be displayed
    #         option (String): The option that will be displayed
    #         Displays the image on the screen, such as the police station
    #     """
    #     # Get the indices of the fields in the 2x2 square
    #     self.numbers+=1
    #     temp = True
    #     square_indices = []
    #     square_indices = self.overlap(police_pos, square_indices)
    #     for i, fld in enumerate(self.fields):
    #             if i in square_indices and fld.road:
    #                 temp = False
    #                 break;
    #     big_image, top_left = self.drawBorder(police_pos, square_indices, img, temp, fld)
    #     for i, fld in enumerate(self.fields):
    #             if i in square_indices:
    #                 fld.building = option + str(self.numbers)
    #                 fld.img = big_image  # Assign the single image surface to each field
    #                 fld.image_rect = big_image.get_rect(topleft=top_left)
    #                 print(fld.building);  
    #                 if option == "police":
    #                     print("Adding police to sat")
    #                     fld.zone.police = True
    #                     fld.zone.addWorkers(self.City)
    #                     fld.zone.satsifaction(self.City)
    #                 elif option == "stadium":
    #                     fld.zone.stadium = True
    #                     fld.zone.addWorkers(self.City)
    #                     fld.zone.satsifaction(self.City)
    #                 print(fld.building);       
    #     if option == "police":
    #         self.City.polCnt += 1
    #     elif option == "stadium":
    #         self.City.StadCnt += 1
    #     # pg.display.flip()

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
            # self.image_rect = scaled_image.get_rect(center=border_rect.center)
            # self.image_rect[] = scaled_image.get_rect(center=border_rect.center)
            # self.screen.blit(scaled_image, image_rect)\
            # fld.image_rect = scaled_image.get_rect(center=fld.rect.center)
            self.selectedBuilding = ""
            big_image = pg.Surface((self.field_size*2, self.field_size*2))
            big_image.fill((86, 148, 70))
            big_image.blit(scaled_image, (0, 0))  # Blit the scaled image onto the big_image surface
            for i, fld in enumerate(self.fields):
                if i in square_indices:
                    fld.building = option + str(self.numbers)
                    fld.Bimg = big_image  # Assign the single image surface to each field
                    fld.image_rect = big_image.get_rect(topleft=top_left)
                    print(fld.building); 
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


    
    # set the Road
    def setRoad(self, police_pos):
        """_summary_
        Args:
            police_pos (tuple): The position of the police station
            Sets the road on the screen and the field
        """
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
        
        
        

    

            
            

    def initializeFields(self):  # initialize the fields, adding them to fields array
        """_summary_
        Initializes the fields and adds them to the fields array
        """
        for row in range(2, self.grid_rows): # starting from 3rd row as first 3 rows are for menu
            for col in range(self.grid_cols):
                x = col * self.field_size
                y = row * self.field_size
                fld = Field(x, y, self.field_size)
                fld.grid_pos = (row, col)
                zone = general("general",0, 0)
                zone.x = fld.x; zone.y = fld.y; fld.zone = zone;
                fld.id = (row*10)+col
                zone.width = 50
                zone.height = 50
                self.fields.append(fld)
                
                

    def initialRoad(self):
        """Initializes the road in the middle of the screen"""
        cnt = 0
        for fld in self.fields:
            cnt+=1;
            row, col = fld.grid_pos
            if row == (self.grid_rows) // 2 or col == (self.grid_cols) // 2:
                fld.color = (65, 65, 65)  # set color to grey for middle field
                fld.road = True;
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
                



    def buildingEvents(self, event_list, police_pos):
        """_summary_
        Args:
            event_list (list): List of events
            police_pos (tuple): The position of the police station
            Handles the events for the buildings
        """
        if (self.selectedBuilding != "" and self.clicks == 2):
                                if (self.selectedBuilding == "police"):
                                    print("Inside  police events")
                                    self.setBigImg(police_pos, "my_game/Assets/police.png", "police")
                                elif(self.selectedBuilding == "road"): 
                                    self.setRoad(police_pos)
                                elif(self.selectedBuilding == "stadium"):
                                    self.setBigImg(police_pos, "my_game/Assets/stadium.png", "stadium")
                                elif (self.selectedBuilding == "tree"):
                                    self.setImg(police_pos, "my_game/Assets/tree.png", "forest")
                                    self.drawTree(police_pos)
                                elif (self.selectedBuilding == "reclassify"):
                                    self.reclassify(police_pos)
                                elif (self.selectedBuilding == "demolish"):
                                    self.removeBigImg(police_pos)
    def zoneEvents(self, event_list, police_pos):
        """_summary_
        Args:
            event_list (list): List of events
            police_pos (tuple): The position of the police station
            Handles the events for the Zones
        """
        if(self.zoneChosed != "" and self.clicks == 2):
                                
                                if(self.zoneChosed == "Residential"):
                                    self.drawZone(police_pos, "my_game/Assets/house.png", "Residential")
                                    # self.City.helpCitizens(self.fields)
                                elif(self.zoneChosed == "Commercial"):
                                    self.drawZone(police_pos, "my_game/Assets/police.png", "Service")
                                elif(self.zoneChosed == "Industrial"):
                                    self.drawZone(police_pos, "my_game/Assets/factory.png", "Industrial")
                                else:
                                    print("No zone choosed") 
                                self.update()

        
        

    def events(self, event_list):
        """_summary_
        Args:
            event_list (list): list of events
            Handles the events
        """
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
                            print(self.clicks)
                            self.buildingEvents(event_list, police_pos)
                            print(f"zone chosed {self.zoneChosed} and clicks {self.clicks}")
                            self.zoneEvents(event_list, police_pos)
                            

                    

   
                                  
    #and field.zone != None
    def update(self):
        """
        Updates the screen
        """
        for field in self.fields: # this will keep the fields updated
            # and  field.zone.typ == "general"
            if (field.building == "" and  field.zone.typ == "general"):
                pg.draw.rect(self.screen, field.color, field.rect)

    # addition of the bacground image
    def addBackground(self):
        """
        Adds the background image
        """
        bg = pg.image.load("my_game/Assets/bg1.png")
        bg = pg.transform.scale(bg, (900, 600))
        self.screen.blit(bg, (0, 0))

    def drawGrid(self):
        """
        Draws the grid
        """
        for x in range(0, self.screen.get_width(), self.field_size):  # drawing vertical lines
            pg.draw.line(self.screen, (255, 255, 255), (x, 100), (x, self.screen.get_height()),1)
        for y in range(100, self.screen.get_height(), self.field_size):  # drawing horizonal lines
            pg.draw.line(self.screen, (255, 255, 255), (0, y), (self.screen.get_width(), y),1)
            
            
    def draw(self):
        """
        Draws the screen
        """
        self.initialRoad()
        self.drawGrid()
        # pg.display.flip()
        
      
      
    def drawDDOne(self, event_list):
        """_summary_

        Args:
            event_list (list): list of events
            Draws the second dropdown menu
        """
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
        list1 = Dropdown(pg.font.SysFont(None, 30),740, 0, 50, 30,"Zones", [commercial, industrial, residential], image)
        selected_option = list1.updateDD(event_list)
        if selected_option >= 0:
            if selected_option == 0:
                print("General")
                # pyautogui.prompt(text='', title='Enter Amout of Tax' , default='')
                self.zoneChosed = "Commercial"
                # pyautogui.alert(" Commercial Zone is Selected")
                self.clicks =0;
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
    
    def drawDDTwo(self, event_list):
        """_summary_

        Args:
            event_list (list): list of events
            Draws the second dropdown menu
        """
        image = pg.image.load("./GUIGame/Buttons/zones.png")
        imgSize = (image.get_width(), image.get_height())    
        forest = pg.image.load("./GUIGame/Buttons/Forest.png");forest = pg.transform.scale(forest, imgSize)
        forBut = Button(0, 0, forest, 1);forBut.setText("Forest")
        pol = pg.image.load("./GUIGame/Buttons/police.png");pol = pg.transform.scale(pol, imgSize)
        police = Button(0, 0, pol, 1);police.setText("Police")
        stad = pg.image.load("./GUIGame/Buttons/stad.png");stad = pg.transform.scale(stad, imgSize)
        stadium = Button(0, 0, stad, 1);stadium.setText("Stadium")
        road = pg.image.load("./GUIGame/Buttons/road.png");road = pg.transform.scale(road, imgSize)
        roadBut = Button(0, 0, road, 1);roadBut.setText("Road")
        image_build = pg.image.load("./GUIGame/Buttons/build.png")
        list2 = Dropdown(pg.font.SysFont(None, 30), 660, 0, 50, 30, "Build",
                               [police, stadium, roadBut], image_build)
        selected_option2 = list2.updateDD(event_list)
        if selected_option2 >= 0:
            if selected_option2 == 0:  
                paug.alert("Police is Selected")
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
            else:
                print("No option selected")
            list2.main = list2.options[selected_option2]
        list2.drawDD(self.screen)
        
       

    
    
    def drawDD(self, event_list):
        """_summary_
        Args:
            event_list (_type_): _description_
            Draws the dropdown menus
        """
        self.drawDDOne(event_list)
        self.drawDDTwo(event_list)
        image = pg.image.load("./GUIGame/Buttons/zones.png")
        imgSize = (image.get_width(), image.get_height())
        buttImg = pg.image.load("./GUIGame/Buttons/oth.png")
        buttImg =  pg.transform.scale(buttImg, imgSize)
        dem = pg.image.load("./GUIGame/Buttons/dem.png");dem = pg.transform.scale(dem, imgSize)
        demolsih = Button(0, 0, dem, 1);demolsih.setText("demolish")
        reclas = pg.image.load("./GUIGame/Buttons/reclas.png");reclas = pg.transform.scale(reclas, imgSize)
        reclass = Button(0, 0, reclas, 1);reclass.setText("reclass")      
        list3 = Dropdown(pg.font.SysFont(None, 30), 820, 0, 50, 30, "Other", [demolsih, reclass], buttImg)
        selected_option3 = list3.updateDD(event_list)
        # print(selected_option2);
        if selected_option3 >= 0:
            if selected_option3 == 0:
                print("Demolish")
                # pyautogui.prompt(text='', title='Enter Amout of Tax' , default='')
                self.selectedBuilding = "demolish"
                self.clicks =0
                # pyautogui.prompt(text='', title='Enter Amout of Tax' , default='
            elif selected_option3 == 1:
                print("Reclassify")
                # pyautogui.alert(" Stadium is Selected")
                self.selectedBuilding = "reclassify"
                self.clicks = 0
            else:
                print("No option selected")
            list3.main = list3.options[selected_option3]
        list3.drawDD(self.screen)
        self.drawFMenu(event_list)
        
        pg.display.flip()
    
    
    def drawFMenu(self,event_list):
        """_summary_
        Args:
            event_list (_type_): _description_
            Draws the dropdown menus
        """
        image = pg.image.load("./GUIGame/Buttons/zones.png")
        imgSize = (image.get_width(), image.get_height())
        feat = pg.image.load("./GUIGame/Buttons/feat.png")
        feat = pg.transform.scale(feat, imgSize)  
        dem = pg.image.load("./GUIGame/Buttons/Forest.png");dem = pg.transform.scale(dem, imgSize)
        demolsih = Button(0, 0, dem, 1);demolsih.setText("demolish")
        reclas = pg.image.load("./GUIGame/Buttons/dis.png");reclas = pg.transform.scale(reclas, imgSize)
        reclass = Button(0, 0, reclas, 1);reclass.setText("disaster")

        list3 = Dropdown(pg.font.SysFont(None, 30), 570, 0, 50, 30, "Other", [demolsih, reclass], feat)
        selected_option3 = list3.updateDD(event_list)
        # print(selected_option2);
        if selected_option3 >= 0:
            if selected_option3 == 0:
                print("Forest")
                # pyautogui.prompt(text='', title='Enter Amout of Tax' , default='')
                self.selectedBuilding = "tree"
                
                
              
                self.clicks =0
                # pyautogui.prompt(text='', title='Enter Amout of Tax' , default='
            elif selected_option3 == 1:
                print("Reclassify")
                # pyautogui.alert(" Stadium is Selected")
                num = 0
                explosion_duration = 6000
                spawn_time = pygame.time.get_ticks()  # initialize timer
                explosion_end_time = spawn_time + explosion_duration  # calculate when explosions should stop
                while num < 5:
                    current_time = pygame.time.get_ticks()
                    if current_time - spawn_time > 1000 and current_time < explosion_end_time:
                        self.show_explosion()  # spawn explosion
                        spawn_time = current_time  # reset timer
                        print(num)
                        num+=1
                self.clicks = 0
            else:
                print("No option selected")
            list3.main = list3.options[selected_option3]
        list3.drawDD(self.screen)
        self.changeDD(event_list)
        
        # pg.display.flip()
    
    
    def changeDD(self, event_list):
        """_summary_
        Args:
            event_list (List): List of events
            DD to change the speed, tax and city name
        """
        image = pg.image.load("./GUIGame/Buttons/zones.png")
        imgSize = (image.get_width(), image.get_height())
        feat = pg.image.load("./GUIGame/Buttons/opt.png")
        feat = pg.transform.scale(feat, imgSize)  
        dem = pg.image.load("./GUIGame/Buttons/name.png");dem = pg.transform.scale(dem, imgSize)
        demolsih = Button(0, 0, dem, 1);demolsih.setText("dem")
        reclas = pg.image.load("./GUIGame/Buttons/speed.png");reclas = pg.transform.scale(reclas, imgSize)
        reclass = Button(0, 0, reclas, 1);reclass.setText("reclass")
        tax = pg.image.load("./GUIGame/Buttons/tax.png");reclas = pg.transform.scale(tax, imgSize)
        taxBut = Button(0, 0, reclas, 1);taxBut.setText("tax")
        list3 = Dropdown(pg.font.SysFont(None, 30), 490, 0, 50, 30, "Other", [demolsih, reclass, taxBut], feat)
        selected_option3 = list3.updateDD(event_list)
        if selected_option3 >= 0:
            if selected_option3 == 0:
                print("name")
                # YOUR CODE HERE
                # pyautogui.prompt(text='', title='Enter Amout of Tax' , default='
            elif selected_option3 == 1:
                print("speed")
                # pyautogui.alert(" Stadium is Selected")
                # YOUR CODE HERE
            elif selected_option3 == 2:
                print("tax")
                # YOUR CODE HERE
            else:
                print("No option selected")
            list3.main = list3.options[selected_option3]
        list3.drawDD(self.screen)
        
        







