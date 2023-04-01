import pygame, sys
from button import Button

class MainMenu():
   pygame.init()
   SCREEN_W = 800
   SCREEN_H = 600
   screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))
   pygame.display.set_caption("Main Menu")

   # game variables
   menu_state = "main"

   # load button images
   start_game = pygame.image.load("Buttons/start_game.png")
   instructions = pygame.image.load("Buttons/instructions.png")

   # button instances
   start_button = Button(350, 500, start_game,1)
   ins_button = Button(350, 300, instructions,1)

   run = True
   while run:
      if menu_state == "main":
         screen.fill((0,0,0))
         if start_button.draw(screen):
            menu_state = "start"
            if ins_button.draw(screen):
               menu_state = "instructions"

   #event handler
   for event in pygame.event.get():
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_SPACE:
        game_paused = True
    if event.type == pygame.QUIT:
      run = False

   pygame.display.update()

pygame.quit()
