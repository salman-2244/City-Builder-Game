import unittest
import pygame as pg
from Game import Game

class TestGame(unittest.TestCase):

    def test_grid_drawing(self):
        pg.init()
        screen = pg.display.set_mode((600, 600)) #create a screen object with dimensions
        clock = pg.time.Clock() # create a clock object for setting frame rate
        game = Game(screen, clock) # create an instance of the Game class
        game.draw_grid() # call the draw_grid() method to draw the grid
        pixels = pg.surfarray.array3d(screen) # get the RGB values of the screen
        expected_color = (0, 0, 0) # expected color for grid line
        for i in range(screen.get_height()):
            for j in range(screen.get_width()):
                if j % game.field_size == 0 or i % game.field_size == 0:
                    self.assertEqual(pixels[i][j].tolist(), expected_color) # check if the RGB values match
