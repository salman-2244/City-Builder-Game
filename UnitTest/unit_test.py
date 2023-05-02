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

    def setUp(self):
        pg.init()
        self.screen = pg.display.set_mode((800, 600))
        self.your_class = YourClass(self.screen)

    def test_setImg(self):
        police_pos = (0, 0)
        img = "police.png"
        self.your_class.setImg(police_pos, img)
        for fld in self.your_class.fields:
            if fld.rect.collidepoint(police_pos) and fld.building == "house":
                # Check that police image was loaded and displayed correctly
                self.assertIsInstance(self.your_class.police_img, pg.Surface)
                self.assertEqual(self.your_class.police_img.get_size(), (50, 50))
                self.assertEqual(fld.building, "house")
                police_rect = self.your_class.police_img.get_rect()
                police_rect.center = fld.rect.center
                self.assertEqual(self.your_class.screen.get_at(police_rect.center), (255, 255, 255,255))
                # Check that border was drawn around the field
                border_rect = pg.Rect(fld.rect.topleft, (self.your_class.field_size, self.your_class.field_size))
                self.assertEqual(self.your_class.screen.get_at(border_rect.midtop), (255, 0, 0, 255))
                self.assertEqual(self.your_class.screen.get_at(border_rect.midbottom), (255, 0, 0, 255))
                self.assertEqual(self.your_class.screen.get_at(border_rect.midleft), (255, 0, 0, 255))
                self.assertEqual(self.your_class.screen.get_at(border_rect.midright), (255, 0, 0, 255))
