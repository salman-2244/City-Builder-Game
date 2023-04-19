import pygame as pg  # importing pygame as pg
from Field import Field
import sys
sys.path.append('./GUIGame')  # importing sys library
from pygame.locals import *  # So I can use the draw module.
from Dropdown import Dropdown 

import time
import test
"""from my_game.test import SelectionRect
import pygame, pygame.surfarray
from pygame.locals import *
import numpy, copy"""


class Game:  # initiating game class.

    def __init__(self, screen, clock):
        self.screen = screen  # setting screen object to screen
        self.clock = clock  # setting clock object
        self.field_size = 30  # size of each field
        self.grid_rows = int(screen.get_height() / self.field_size)  # calculate rows (use later)
        self.grid_cols = int(screen.get_width() / self.field_size)  # calculate cols
        self.line_width = 1  # width of grid lines
        self.fields =  [] # array of field class.
        self.initializeFields()  # initialize fields of 30 px each on screen
        self.dragging = False  # check if the user is draging or not

    def run(self):
        self.playing = True  # untill player is playing it will be true
        self.timer = 0  # starter for timer
        while self.playing:  # while player is playing
            self.clock.tick(60)  # limiting the game loop to a maximum of 60 frames per second
            self.events()
            self.update()
            self.draw()

    def initializeFields(self):  # initialize the fields, adding them to fields array
         for row in range(3, self.grid_rows): # starting from 3rd row as first 3 rows are for menu
            for col in range(self.grid_cols):
                x = col * self.field_size
                y = row * self.field_size
                fld = Field(x, y, self.field_size)
                fld.grid_pos = (row, col)
                self.fields.append(fld)
                rect = pg.Rect(x, y, self.field_size, self.field_size)
                

    def initialRoad(self):
        # Change the color of fields in the middle to grey
        for fld in self.fields:
            row, col = fld.grid_pos
            if row == (self.grid_rows) // 2 or col == (self.grid_cols) // 2:
                fld.color = (65, 65, 65)  # set color to grey for middle field
                fld.road = True;

    def events(self):
        for event in pg.event.get(): # getting all events
            if event.type == pg.QUIT: # if player click exit then exit
                pg.quit();
                sys.exit()
            elif event.type == pg.KEYDOWN:  # if key is pressed
                if event.key == pg.K_ESCAPE: # if player press esc key then exit
                     pg.quit();
                     sys.exit();
            elif event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1:  # if left mouse button is pressed
                    self.dragging = True
                   
            elif event.type == pg.MOUSEBUTTONUP:
                if event.button == 1:  # if left mouse button is released
                    self.dragging = False
            elif event.type == pg.MOUSEMOTION:
                if self.dragging:  # if left mouse button is held down and mouse is moving

                    for field in self.fields:
                        if field.rect.collidepoint(event.pos) and field.selected == False and field.road == False:
                            field.color = (255, 0, 0)
                            field.selected = True;

    def update(self):
        pass;

    # addition of the bacground image
    def addBackground(self):
        bg = pg.image.load("my_game/Assets/bg.jpg")
        bg = pg.transform.scale(bg, (900, 600))
        self.screen.blit(bg, (0, 0))

    def drawGrid(self):

        for x in range(0, self.screen.get_width(), self.field_size):  # drawing vertical lines
            pg.draw.line(self.screen, (255, 255, 255), (x, 90), (x, self.screen.get_height()),1)
        for y in range(90, self.screen.get_height(), self.field_size):  # drawing horizonal lines
            pg.draw.line(self.screen, (255, 255, 255), (0, y), (self.screen.get_width(), y),1)


    def draw(self):
        pg.init()  # initializing pygame
        image = pg.image.load(
            "./GUIGame/Buttons/zones.png")
        clock = pg.time.Clock()
        # for the zone dropdown menu
        list1 = Dropdown(pg.font.SysFont(None, 30),
                         700, 0, 50, 30,
                         "Zones", ["General", "Residential", "Commercial", "Industrial"], image)
        image_build = pg.image.load(
            "./GUIGame/Buttons/build.png")
        list2 = Dropdown(pg.font.SysFont(None, 30), 600, 0, 50, 30, "Build",
                              ["Police", "Forest", "Stadium", "Road"], image_build)
        run = True

        # screen = pygame.display.set_mode((640,480),0,24)
        screen = self.screen
        # create a dotted background
        """bg = pygame.image.load(
            "/Users/markoboreta/Dropbox/Semester 6/City_builder/Pyton_G/blue-fox/my_game/Assets/bg.jpg")
        bg = pygame.transform.scale(bg, (900, 600))"""

        
        pg.display.update()

        # make up a test loop
        finished = 0
        selection_on = 0
        self.drawGrid()
        zonesCond = False
        run = True
        while run:
            self.timer += 1 # incrementing timer
            clock.tick(100)

            event_list = pg.event.get()
            for event in event_list:
                if event.type == pg.QUIT:
                     run = False

            #for the zone dropdown menu
            selected_option = list1.update(event_list)
            if selected_option >= 0:
                 list1.__main = list1.options[selected_option]
                 print("Selected option: ", list1.options[selected_option])
                 if list1.options[selected_option] == "General":
                     print("General zone selected")
                     self.run()
                 elif list1.options[selected_option] == "Residential":
                     print("Residential zone selected")

                     # Residential zone selected to be added here
                 elif list1.options[selected_option] == "Commercial":
                     print("Commercial zone selected")
                 elif list1.options[selected_option] == "Industrial":
                     print("Industrial zone selected")
                 else:
                     print("Error")

            #self.fill((255, 255, 255))
            list1.draw(self.screen)

            #for the build dropdown menu
            selected_option_2 = list2.update(event_list)
            if selected_option_2 >= 0:
                 list2.__main = list2.options[selected_option_2]
                 print("Selected option: ", list2.options[selected_option_2])
                 if list2.options[selected_option_2] == "Police":
                     print("Police to build selected")
                 elif list2.options[selected_option_2] == "Forest":
                     print("Forest to build selected")
                 elif list2.options[selected_option_2] == "Stadium":
                     print("Stadium to build selected")
                 elif list2.options[selected_option_2] == "Road":
                     print("Road to build selected")
                     # FUnct for road to be added here
                 else:
                     print("Error")
            list2.draw(self.screen)
            pg.display.flip()
        pg.quit()
        exit()


        """while not finished:
            self.timer += 1 # incrementing timer
            clock.tick(100)

            event_list = pg.event.get()
            for event in event_list:
                if event.type == pg.QUIT:
                     run = False

                for e in pg.event.get():

                        if e.type == QUIT or (e.type == KEYDOWN and e.key == K_ESCAPE):
                            finished = 1
                        elif e.type == MOUSEBUTTONDOWN and e.button == 1:
                            if not selection_on:
                                # begin with selection as the user pressed down the left
                                # mouse button
                                selection_on = 1
                                selection = SelectionRect(self.screen,e.pos)
                        elif e.type == MOUSEMOTION:
                            if selection_on:
                                # update the selection rectangle while the mouse is moving
                                selection.updateRect(e.pos)
                                selection.draw(self.screen)
                        elif e.type == MOUSEBUTTONUP and e.button == 1:
                            if selection_on:
                                # stop selection when the user released the button
                                selection_on = 0
                                rect = selection.updateRect(e.pos)
                                # don't forget this!
                                # (or comment it out if you really want the final selection
                                #  rectangle to remain visible)
                                selection.hide(self.screen)
                                # just FYI
                                print ("Final selection rectangle:",rect)
                                print(e.pos)

            #for the zone dropdown menu
            selected_option = list1.update(event_list)
            if selected_option >= 0:
                 list1.__main = list1.options[selected_option]
                 print("Selected option: ", list1.options[selected_option])
                 self.drawGrid()
                 if list1.options[selected_option] == "General":

                      print("General zone selected")
                      #self.addBackground()

                 elif list1.options[selected_option] == "Residential":
                     print("Residential zone selected")

                     # Residential zone selected to be added here
                 elif list1.options[selected_option] == "Commercial":
                     print("Commercial zone selected")
                 elif list1.options[selected_option] == "Industrial":
                     print("Industrial zone selected")
                 else:
                     print("Error")

            #self.fill((255, 255, 255))
            list1.draw(self.screen)

            #for the build dropdown menu
            selected_option_2 = list2.update(event_list)
            if selected_option_2 >= 0:
                 list2.__main = list2.options[selected_option_2]
                 print("Selected option: ", list2.options[selected_option_2])
                 if list2.options[selected_option_2] == "Police":
                     print("Police to build selected")
                 elif list2.options[selected_option_2] == "Forest":
                     print("Forest to build selected")
                 elif list2.options[selected_option_2] == "Stadium":
                     print("Stadium to build selected")
                 elif list2.options[selected_option_2] == "Road":
                     print("Road to build selected")
                     # FUnct for road to be added here
                 else:
                     print("Error")
            list2.draw(self.screen)
            pg.display.update()

        """









