import pygame as pg  # importing pygame as pg
from Field import Field
import sys  # importing sys library
from pygame.locals import *  # So I can use the draw module.


class Game:  # initiating game class.

    def __init__(self, screen, clock):
        self.screen = screen  # setting screen object to screen
        self.clock = clock  # setting clock object
        self.field_size = 30  # size of each field
        self.grid_rows = int(screen.get_height() / self.field_size)  # calculate rows (use later)
        self.grid_cols = int(screen.get_width() / self.field_size)  # calculate cols
        self.line_width = 1  # width of grid lines
        self.fields = []
        self.initializeFields()
        self.dragging = False


    def initializeFields(self):
        for row in range(3, self.grid_rows):
            for col in range(self.grid_cols):
                x = col * self.field_size
                y = row * self.field_size
                fld = Field(x, y, self.field_size)
                fld.grid_pos = (row, col)
                self.fields.append(fld)
                rect = pg.Rect(x, y, self.field_size, self.field_size)
                # pg.draw.rect(self.screen, (100, 100, 100), rect)
                # pg.draw.rect(self.screen, (255, 255, 255), rect, 1)

    def run(self):
        self.playing = True
        self.timer = 0
        while self.playing:  # while player is playing
            self.clock.tick(60)  # limiting the game loop to a maximum of 60 frames per second
            self.events()
            self.update()
            self.draw()

    def events(self):
        dragging = False
        for event in pg.event.get():  # getting all events
            if event.type == pg.QUIT:  # if player click exit then exit
                pg.quit();
                sys.exit()
            elif event.type == pg.KEYDOWN:  # if key is pressed
                if event.key == pg.K_ESCAPE:  # if player press esc key then exit
                    pg.quit();
                    sys.exit();
            elif event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1:  # if left mouse button is pressed
                    self.dragging = True
                    print(dragging)
            elif event.type == pg.MOUSEBUTTONUP:
                if event.button == 1:  # if left mouse button is released
                    self.dragging = False
                    print(dragging)
            elif event.type == pg.MOUSEMOTION:
                if self.dragging:  # if left mouse button is held down and mouse is moving
                    print('sffd')
                    for field in self.fields:
                        if field.rect.collidepoint(event.pos) and field.selected == False:
                            field.color = (255, 0, 0)
                            field.selected = True;

    # self.select_field()

    def update(self):
        pass;

    #addition of the bacground image
    def addBackground(self):
        bg = pg.image.load("./Assets/bg.jpeg")
        bg = pg.transform.scale(bg, (900, 600))
        self.screen.blit(bg, (0, 0))

    def drawGrid(self):
        # self.addBackground()
        for x in range(0, self.screen.get_width(), self.field_size):  # drawing vertical lines
            pg.draw.line(self.screen, (255, 255, 255), (x, 90), (x, self.screen.get_height()), self.line_width)
        for y in range(90, self.screen.get_height(), self.field_size):  # drawing horizonal lines
            pg.draw.line(self.screen, (255, 255, 255), (0, y), (self.screen.get_width(), y), self.line_width)

    def draw(self):
        self.addBackground()
        #self.screen.fill((0, 0, 0))  # fill the screen
        for field in self.fields:
            pg.draw.rect(self.screen, field.color, field.rect)
        self.drawGrid()  # drawing the grid
        pg.display.flip();  # update the changes in display
