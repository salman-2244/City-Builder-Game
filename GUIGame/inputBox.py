import pygame as pg


pg.init()
screen = pg.display.set_mode((640, 480))
COLOR_INACTIVE = pg.Color('lightskyblue3')
COLOR_ACTIVE = pg.Color('dodgerblue2')
FONT = pg.font.Font(None, 32)


class InputBox:

    def __init__(self, x, y, w, h, text=''):
        self.rect = pg.Rect(x, y, w, h)
        self.color = COLOR_INACTIVE
        self.text = text
        self.txt_surface = FONT.render(text, True, self.color)
        self.active = False
    
    
    def clicked(self, mouse):
        if self.rect.collidepoint(mouse):
            return True
        else:
            return False
    
    
    def handle_event(self, event_list):
        for event in event_list:
            if event.type == pg.MOUSEBUTTONDOWN:
                # If the user clicked on the input_box rect.
                if self.clicked(event.pos):
                    # Toggle the active variable.
                    print('Colided')
                    self.active = not self.active
                else:
                    self.active = False
                # Change the current color of the input box.
                print(self.active)
                self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE
            if event.type == pg.KEYDOWN:
                if self.active:
                    if event.key == pg.K_RETURN:
                        print(self.text)
                        self.text = ''
                    elif event.key == pg.K_BACKSPACE:
                        self.text = self.text[:-1]
                    else:
                        self.text += event.unicode
                    # Re-render the text.
                    self.txt_surface = FONT.render(self.text, True, self.color)

    def update(self):
        # Resize the box if the text is too long.
        width = max(200, self.txt_surface.get_width()+10)
        self.rect.w = width
    
    def getText(self):
        return self.text

    def draw(self, screen):
        # Blit the text.
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        # Blit the rect.
        pg.draw.rect(screen, self.color, self.rect, 2)


def inGameBox(screen, x, y, w, h, text=''):
    input_box = InputBox(x, y, w, h, text)
    input_box.update()
    screen.fill((30, 30, 30))
    input_box.draw(screen)
    pg.display.flip()
    return input_box.getText()

# def main():
#     clock = pg.time.Clock()
#     input_box1 = InputBox(100, 100, 140, 32)
#     input_box2 = InputBox(100, 300, 140, 32)
#     input_boxes = [input_box1, input_box2]
#     done = False

    
#     while not done:
#         events = pg.event.get()
#         for event in events:
#             if event.type == pg.QUIT:
#                 done = True
#             for box in input_boxes:
#                 box.handle_event(events)

#         for box in input_boxes:
#             box.update()

#         screen.fill((30, 30, 30))
#         for box in input_boxes:
#             box.draw(screen)

#         pg.display.flip()
#         clock.tick(30)


# if __name__ == '__main__':
#     main()
#     pg.quit()