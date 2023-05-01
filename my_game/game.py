import pygame as pg  # importing pygame as pg
from Field import Field
import sys
sys.path.append('./Zones')  # importing sys library
sys.path.append('./GUIGame')
from pygame.locals import *  # So I can use the draw module.
from Dropdown import Dropdown
from button import Button
from City import City
from menuBar import menuBar
import datetime
import test
from inputBox import InputBox
from zone import inudstrial, residential, zone

class Game(pg.sprite.Sprite):  # initiating game class.

    def __init__(self, screen, clock):
        super().__init__()
        self.screen = screen  # setting screen object to screen
        self.clock = clock  # setting clock object
        self.field_size = 30  # size of each field
        self.grid_rows = int(screen.get_height() / self.field_size)  # calculate rows (use later)
        self.grid_cols = int(screen.get_width() / self.field_size)  # calculate cols
        self.line_width = 1  # width of grid lines
        self.fields =  [] # array of field class.
        self.dragging = False  # check if the user is draging or not
        self.City = City("New York City", 18, 50) # creating a city object 
        self.zoneChosed = ""
        self.zoneChosedType = ""
        self.zoneNo = 0
        self.initializeFields()  # calling initializeFields function
        self.time_elapsed = pg.time.get_ticks()
        self.speed = 1
        # self.addBackground()
        
        
    def setImg(self, police_pos, img):
        police_img = pg.image.load(img)
        newSize = (50, 50)
        scaled_image = pg.transform.scale(police_img, newSize)
        print(police_pos)
        for i, fld in enumerate(self.fields):
            if fld.rect.collidepoint(police_pos) and fld.building == "":
                fld.building = "house";
                police_rect = scaled_image.get_rect()
                police_rect.center = fld.rect.center
                self.screen.blit(scaled_image, police_rect)
                # Draw border around the field
                border_rect = pg.Rect(fld.rect.topleft, (self.field_size, self.field_size))
                pg.draw.rect(self.screen, (255, 0, 0), border_rect, 3)
        pg.display.flip()
        
        
    def setBigImg(self, police_pos, img):
        # Get the indices of the fields in the 2x2 square
        square_indices = []
        for i, fld in enumerate(self.fields):
            if fld.rect.collidepoint(police_pos):
                if (i % self.grid_cols < self.grid_cols - 1) and (i // self.grid_cols < self.grid_rows - 1):
                    if fld.building != "":
                        print("Cannot oveerlap Stadium")
                        prompt_message = "Enter your name: "
                        prompt_text = self.font.render(prompt_message, True, (255, 255, 255))
                        prompt_rect = prompt_text.get_rect(center=(300, 500))
                        self.screen.blit(prompt_text, prompt_rect)
                        pg.display.update()
                        break
                        
                    square_indices.extend([i, i+1, i+self.grid_cols, i+self.grid_cols+1])
                    
                    break
    
    # Draw a border around the fields in the 2x2 square
            if square_indices:
                top_left = self.fields[square_indices[0]].rect.topleft
                bottom_right = self.fields[square_indices[-1]].rect.bottomright
                border_rect = pg.Rect(top_left, (bottom_right[0]-top_left[0], bottom_right[1]-top_left[1]))
                pg.draw.rect(self.screen, (250, 100, 100), border_rect, 2)
                # print(square_indices[0]);
                # Load and draw the image in the center of the square
                police_img = pg.image.load(img)
                scaled_image = pg.transform.scale(police_img, (self.field_size*2, self.field_size*2))
                image_rect = scaled_image.get_rect(center=border_rect.center)
                self.screen.blit(scaled_image, image_rect)
                
                for i, fld in enumerate(self.fields):
                    if i in square_indices:
                        fld.building = "stadium"
                    print(fld.building);         
                pg.display.flip()

    
    
    def setRoad(self, police_pos):
        print(police_pos)
        for i, fld in enumerate(self.fields):
            if fld.rect.collidepoint(police_pos):
                fld.color = (65, 65, 65)
                print(fld.color);
                print("inside loop")
        pg.display.flip()   
        
        
    # function that will create datetime and we will use it on the menu bar
    def currentTime(self):
        current_time = datetime.datetime.now()
        minutes = current_time.minute 
        hour = current_time.hour
        date = current_time.date()
        # print(f"The current date and the time is: {date}: {hour}: {minutes}")
        
        # font = pg.font.SysFont('Arial', 8)
        # text = (f"Time elapsed: {self.time_elapsed}")
        
        # screen.blit(text, (0, 40))
        return (f"{date}: {hour}: {minutes}")
        # return text
    
        
        
    
    
    def run(self):
        self.playing = True  # untill player is playing it will be true
        self.timer = 0  # starter for timer
        self.addBackground()
        self.drawInfo(self.screen, 50)
        time = 60
        if self.speed == 1:
            time = 60
        elif self.speed == 2:
            time = 40
        elif self.speed == 3:
            time = 20
            
        
        while self.playing:  # while player is playing
            self.currentTime()
            event_list = pg.event.get()
            self.draw(event_list)    
            self.drawDD(event_list)  
            # self.drawDDBox(event_list)
            self.clock.tick(time)  # limiting the game loop to a maximum of 60 frames per second
            
            for zone in self.City.zones:
                if zone.type == "residential":
                    # zone.moveOutAndIn(self.City)
                    pass
            self.events(event_list)
            self.update(event_list)
            
            

    def initializeFields(self):  # initialize the fields, adding them to fields array
         for row in range(4, self.grid_rows): # starting from 3rd row as first 3 rows are for menu
            for col in range(self.grid_cols):
                x = col * self.field_size
                y = row * self.field_size
                fld = Field(x, y, self.field_size)
                fld.grid_pos = (row, col)
                self.fields.append(fld)
                print(len(self.fields))
                rect = pg.Rect(x, y, self.field_size, self.field_size)
                

    def initialRoad(self):
        # Change the color of fields in the middle to grey
        for fld in self.fields:
            row, col = fld.grid_pos
            if row == (self.grid_rows) // 2 or col == (self.grid_cols) // 2:
                fld.color = (65, 65, 65)  # set color to grey for middle field
                fld.road = True;

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
                # if(self.isSelecteBuilding):
                # print("Mouse button down event fired")   
                police_pos = event.pos
                # self.setBigImg(police_pos, "my_game/Assets/stadium.png")
                # self.mess()
                self.setRoad(police_pos)
                    # self.setRoad(police_pos);
            #     mouse_pos = pg.mouse.get_pos()
            #     for i, fld in enumerate(self.fields):
            #         if fld.rect.collidepoint(mouse_pos):
            #             print("Clicked on field", i)
            #             self.click_count+=1;
            #     if event.button == 1:  # if left mouse button is pressed
            #         self.dragging = True
                   
            # elif event.type == pg.MOUSEBUTTONUP:
            #     if event.button == 1:  # if left mouse button is released
            #         self.dragging = False
            # elif event.type == pg.MOUSEMOTION:
            #     if self.dragging:  # if left mouse button is held down and mouse is moving

            #         for field in self.fields:
            #             # and field.road == False
            #              if field.rect.collidepoint(event.pos) and field.selected == False :
            #                 field.color = (255, 0, 0)
            #                 field.selected = True;
            #         pg.display.flip()

    def update(self, event_list):
        # self.addBackground()
        self.draw(event_list)
        self.buildZone(event_list)
        self.drawInfo(self.screen, 50)
        

    # addition of the bacground image
    def addBackground(self):
        bg = pg.image.load("my_game/Assets/bg.jpg")
        bg = pg.transform.scale(bg, (900, 600))
        self.screen.blit(bg, (0, 0))
        


    def drawGrid(self):
        for x in range(0, self.screen.get_width(), self.field_size):  # drawing vertical lines
            pg.draw.line(self.screen, (255, 255, 255), (x, 120), (x, self.screen.get_height()),1)
        for y in range(120, self.screen.get_height(), self.field_size):  # drawing horizonal lines
            pg.draw.line(self.screen, (255, 255, 255), (0, y), (self.screen.get_width(), y),1)
    
    
    # draw the info part of the menu in the blue bar
    def drawInfo(self, screen, value):
        
        happiness = 50
        if self.City.population > 0:
            for zone in self.City.zones:
                if zone.name == "residential":
                    for resident in zone.residents:
                        happiness+= self.resident.happy
            happiness = round((happiness / self.City.population) * 100)
            happiness = str(happiness)+"%"
        
                    
                
        # --------------------- Info ---------------------------------------
        date_and_time = self.currentTime()
        info = [self.City.name, self.City.population, self.City.bank, date_and_time, happiness]
        # font = pg.font.SysFont("comicsansms", 20)
        mb = menuBar(self.screen, 0, 50, screen.get_width(), screen.get_height(), info)# creating a menu bar object
        mb.displayItems(screen, info, value, ) # drawing the menu bars

            
    def draw(self, event_list):
        pass
        #self.addBackground()
        for field in self.fields: # this will keep the fields updated
            pg.draw.rect(self.screen, field.color, field.rect)
        self.drawGrid()
        self.initialRoad()
        

        
        
        pg.display.flip()
        # pg.quit()
        # exit()

    """This function is used to draw the dropdown menu for the zones.
            - event_list: list of events
            it doesnt want to recall back after the first time it is called
            if u know how to fix it please do so
            I tried to kill sprite but it didnt work
            
    """
    
    
    def drawDD(self, event_list):
                # --------------------- Zones list ---------------------------------------
        image = pg.image.load("./GUIGame/Buttons/zones.png")
        imgSize = (image.get_width(), image.get_height())

        
        #---------------------
        ret = ""
        #---------------------
        
        ini = pg.image.load("./GUIGame/Buttons/General.png");ini = pg.transform.scale(ini, imgSize)
        general = Button(0, 0, ini, 1);general.setText("General")
        comm = pg.image.load("./GUIGame/Buttons/Commercial.png");comm = pg.transform.scale(comm, imgSize)
        commercial = Button(0, 0, comm, 1);commercial.setText("Commercial")
        ind = pg.image.load("./GUIGame/Buttons/industrial.png");ind = pg.transform.scale(ind, imgSize)
        industrial = Button(0, 0, ind, 1);industrial.setText("Industrial")
        res = pg.image.load("./GUIGame/Buttons/Res.png");res = pg.transform.scale(res, imgSize)
        residential = Button(0, 0, res, 1);residential.setText("Residential")
        
        # for the zone dropdown menu
        list1 = Dropdown(pg.font.SysFont(None, 30),700, 0, 50, 30,"Zones", [general, commercial, industrial, residential], image)
        selected_option = list1.updateDD(event_list)
        
        if selected_option >= 0:
            if selected_option == 0:
                print("General")
                ret = "General"
                # selection on click herre 
                # code your selection here !!!!!!! 
                
            elif selected_option == 1:
                print("Commercial")
                self.zoneChosed = "Commercial"
                self.update(event_list)
            elif selected_option == 2:
                print("Industrial")
                self.zoneChosed = "Industrial"
                self.update(event_list)
            elif selected_option == 3:
                print("Residential")
                self.zoneChosed = "Residential"
                self.update(event_list)
            else:
                print("No option selected")
                self.zoneChosed = ""
            list1.main = list1.options[selected_option]
        s1 = selected_option
        list1.drawDD(self.screen)
        # spriteGroup = pg.sprite.Group()        
        # ------------------------------- Build list -------------------------------------
        forest = pg.image.load("./GUIGame/Buttons/Forest.png");forest = pg.transform.scale(forest, imgSize)
        forBut = Button(0, 0, forest, 1);forBut.setText("Forest")
        pol = pg.image.load("./GUIGame/Buttons/Police.png");pol = pg.transform.scale(pol, imgSize)
        police = Button(0, 0, pol, 1);police.setText("Police")
        stad = pg.image.load("./GUIGame/Buttons/stad.png");stad = pg.transform.scale(stad, imgSize)
        stadium = Button(0, 0, stad, 1);stadium.setText("Stadium")
        road = pg.image.load("./GUIGame/Buttons/Road.png");road = pg.transform.scale(road, imgSize)
        roadBut = Button(0, 0, road, 1);roadBut.setText("Road")
        image_build = pg.image.load("./GUIGame/Buttons/build.png")
        list2 = Dropdown(pg.font.SysFont(None, 30), 600, 0, 50, 30, "Build",
                               [police, stadium, roadBut, forBut], image_build)
        selected_option2 = list2.updateDD(event_list)
        print(selected_option2)
        if selected_option2 >= 0:
            if selected_option2 == 0:
                print("Police")
                self.zoneChosedType  = "Police"
                self.update(event_list)
            elif selected_option2 == 1:
                print("Stadium")
                self.zoneChosedType  = "Stadium"
                self.update(event_list)
            elif selected_option2 == 2:
                print("Road")
                self.zoneChosedType  = "Road"
                self.update(event_list)
            elif selected_option2 == 3:
                print("Forest")
                self.zoneChosedType  = "Forest"
                self.update(event_list)
            else:
                print("No option selected")
                self.zoneChosedType  = ""
            list2.main = list2.options[selected_option2]
        list2.drawDD(self.screen)
        
        pg.display.flip()
        return ret

    
    
    # def selectZone(self):
        
    
    
    
    
    
    """This function is used to draw the initial road and grid but cleaned up the code"""

    # def drawDDBox(self, event_list):
    #     image = pg.image.load("./GUIGame/Buttons/zones.png")
    #     imgSize = (image.get_width(), image.get_height())
    #     ins_button = Button(20, 0, image, 1)
    #     ins_button.update(self.screen)
    #     input_box1 = InputBox(100, 200, 100, 100)
    #     # input_box2 = InputBox(20, 40, 75, 60)
    #     input_boxes = [input_box1]
    #     RED = (255, 0, 0)
    #     rect_x = 20
    #     rect_y = 30
    #     rect_width = 90
    #     rect_height = 80
    #     text1 = ""
    #     text2 = ""
    #     clicked = 0
        
    #     if ins_button.isClicked(event_list):
    #         clicked += 1
    #         # pg.draw.rect(self.screen, RED, [rect_x, rect_y, rect_width, rect_height])
    #         for box in input_boxes:
    #                 print("Here2")
    #                 if clicked == 1:
    #                     box.handle_event(event_list)
                    
    #         for box in input_boxes:
    #             box.update()
    #             print("Active: ", box.active)
    #             print("here 3")
    #         text1 = input_box1.text
    #         # text2 = input_box2.text
    #         if text1 != "" or text2 != "" and  event.type == pg.KEYDOWN:
    #             if pg.KEYDOWN == pg.K_RETURN:
    #                 print("text1: ", text1)
    #                 # print("text2: ", text2)
    #                 # self.update(event_list)
    #         for box in input_boxes:
    #             box.draw(self.screen)

    #         pg.display.flip()
            
            
    def buildZone(self, event_list):
        print(self.City.population)
        if self.zoneChosed == "Residential":
            self.zoneNo += 1
            zone = residential("res",0,self.zoneNo)
            zone.x = 0
            zone.y = 100
            zone.width = 300
            zone.height = 300
            # zone.initialResidents()
            zone.createInitialResidents(self.City)
            print('Residents no:', self.City.population)
            for i in range (len(zone.residents)):
                print(zone.residents[i].workZone)
            # self.update(event_list)
            
        if self.zoneChosed == "Industrial":
            self.zoneNo += 1
            zone = inudstrial("Indstrial",0,self.zoneNo)
            zone.x = 300
            zone.y = 100
            zone.width = 300
            zone.height = 300
            zone.setMaxEmployees() # max employeees of the zone
            self.City.zones.append(zone)
            zone.addWorkers(self.City)
            print(zone.max_employees)
            print(zone.name + " " + str(zone.num))
            
            
            
            
            
            # self.update(event_list)