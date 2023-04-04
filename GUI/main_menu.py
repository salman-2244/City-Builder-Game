import pygame, sys
from GUI.button import Button

class MainMenu():
  pygame.display.set_caption("Main Menu")

  pygame.init()
  SCREEN_W = 900
  SCREEN_H = 600
  SCREEN = pygame.display.set_mode((SCREEN_W, SCREEN_H))
  pygame.display.set_caption("Main Menu")
  BG = SCREEN.fill((200, 190, 190))# load background

  # game variables
  menu_state = "main"

  # load button images
  start_game = pygame.image.load("Buttons/start_game.png")
  instructions = pygame.image.load("Buttons/instructions.png")

  # button instances
  ins_button = Button(350, 300, instructions, 1)
  start_button = Button(350, 500, start_game, 1)

  while True:
    #SCREEN.blit(BG, (0, 0))
    SCREEN.fill("white")
    MENU_MOUSE_LOC = pygame.mouse.get_pos()
    MENU_TEXT = pygame.font.Font(None).render("MAIN MENU", True, "red")
    MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

    for button in [start_button, ins_button]:
      button.update(SCREEN)

    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
      if event.type == pygame.MOUSEBUTTONDOWN:
        if start_button.checkInput(MENU_MOUSE_LOC):
          print("Clicked play")
        if ins_button.checkInput(MENU_MOUSE_LOC):
          print("Clicked ins")
  pygame.display.update()


  def start(start_button, ins_button, SCREEN):
    while True:
        MOUSE_COORD = pygame.mouse.get_pos()
        SCREEN.fill("black")

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.QUIT
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if start_button.checkInput(MOUSE_COORD):
                    MainMenu()
    pygame.display.update()







