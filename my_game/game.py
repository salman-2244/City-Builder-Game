import pygame as pg # importing pygame as pg
from Field import Field
import sys  # importing sys library
from GUI.Dropdown import Dropdown
from GUI.button import Button
#sfrom my_game.Logic import World

import sys  # importing sys library
from pygame.locals import * # So I can use the draw module.

class Game:  # initiating game class.
    
    def __init__(self, screen, clock):
         self.screen = screen  # setting screen object to screen
         self.clock = clock    # setting clock object
         self.field_size = 30  # size of each field
         self.grid_rows = int(screen.get_height() / self.field_size)  # calculate rows (use later)
         self.grid_cols = int(screen.get_width() / self.field_size)  # calculate cols
         self.line_width = 1   # width of grid lines
         self.fields = []

         
         
    def run(self): 
        self.playing = True 
        self.timer = 0 
        while self.playing: # while player is playing
            self.clock.tick(60) # limiting the game loop to a maximum of 60 frames per second
            self.events() 
            self.update()
            self.draw()
            
            
    def events(self):
        for event in pg.event.get(): # getting all events
            if event.type == pg.QUIT: # if player click exit then exit
                pg.quit();
                sys.exit()
            elif event.type == pg.KEYDOWN:  # if key is pressed
                if event.key == pg.K_ESCAPE: # if player press esc key then exit
                     pg.quit();
                     sys.exit();
            elif event.type == pg.MOUSEBUTTONUP:
                pos = pg.mouse.get_pos()
                print(pos);
                     
    def update(self):
        pass;

    # addition of the bacground image         
    def addBackground(self):
        bg = pg.image.load("assets/bg.jpg")
        bg = pg.transform.scale(bg, (900, 600))
        self.screen.blit(bg, (0, 0))
        
    


    def drawGrid(self):
        
        for x in range(0, self.screen.get_width(), self.field_size): # drawing vertical lines
           pg.draw.line(self.screen, (255, 255, 255), (x, 90), (x, self.screen.get_height()), self.line_width)
        for y in range(90, self.screen.get_height(), self.field_size): # drawing horizonal lines
           pg.draw.line(self.screen, (255, 255, 255), (0, y), (self.screen.get_width(), y), self.line_width) 
           
       
        # for row in range(self.grid_rows):
        #     for col in range(self.grid_cols):
        #         x = col * self.field_size
        #         y = row * self.field_size
        #         field = Field(x, y, self.field_size, None)
        #         self.fields.append(field)
                         
                    
    def draw(self):
        
        image = pg.image.load("/Users/markoboreta/Dropbox/Semester 6/City_builder/Pyton_G/blue-fox/GUI/Buttons/zones.png")
        clock = pg.time.Clock()
        #gen_img = pg.image.load("/Users/markoboreta/Dropbox/Semester 6/City_builder/Pyton_G/blue-fox/GUI/Buttons/start.png")
        self.screen.fill((0, 0, 0)) # fill the screen 
        # for the zone dropdown menu
        l1 = list1 = Dropdown(pg.font.SysFont(None, 30), 
        700, 0, 50, 30,  
        "Zones", ["General", "Residential", "Commercial", "Industrial"], image)
        image_build = pg.image.load("/Users/markoboreta/Dropbox/Semester 6/City_builder/Pyton_G/blue-fox/GUI/Buttons/build.png")
        l2 = list2 = Dropdown(pg.font.SysFont(None, 30), 600, 0, 50, 30, "Build", ["Police", "Forest", "Stadium", "Road"], image_build)
        run = True
        self.screen
        while run:

            self.addBackground()
            self.drawGrid()

             # drawing the grid
            #pg.display.flip();  # update the changes in display
            
            self.timer += 1 # incrementing timer
            clock.tick(100)

            event_list = pg.event.get()
            for event in event_list:
                if event.type == pg.QUIT:
                    run = False

            # for the zone dropdown menu
            selected_option = list1.update(event_list)
            if selected_option >= 0:
                list1.__main = list1.options[selected_option]
                print("Selected option: ", list1.options[selected_option])
                if list1.options[selected_option] == "General":
                    print("General zone selected")

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

            # for the build dropdown menu
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
        
        #world = World()
        #World.init_fields(self, self.screen)
        
        
    
        
    
    

        
        