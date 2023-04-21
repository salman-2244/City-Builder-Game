import pygame
import sys

class Button():
    def __init__(self,  x,y,image,  scale):
        
        width = image.get_width()
        height = image.get_height()
        self.x = x
        self.y = y
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False
        self.text = None
        self.name = " "
        
    def setName(self, name):
        self.name = name
        
    def getRect(self):
        return self.rect

    def setText(self, text):
        if self.image == '':
            self.text = text
    
    def update(self,screen):
        if self.image is not None:
            screen.blit(self.image, self.rect)
        screen.blit(self.image, self.rect)

    def checkInput(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
           return True
        return False

    def isClicked(self, events):
        clicked = False
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()
                clicked = self.checkInput(mouse)
        return clicked
    
    def onClick(self, execute): # execute is a function which we pass to execute on button click
        execute()