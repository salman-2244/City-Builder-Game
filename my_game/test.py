# from typing import Tuple, Any, Optional, List
# import pygame
# import pygame_menu
# from pygame_menu.examples import create_example_window

    
# ZONE = ['General']
# FPS = 60
# WINDOW_SIZE = (640, 480)


# def change_difficulty(value: Tuple[Any, int], zone: str) -> None:
#         """
#         Change difficulty of the game.
#         :param value: Tuple containing the data of the selected object
#         :param difficulty: Optional parameter passed as argument to add_selector
#         """
#         selected, index = value
#         print(f'Selected difficulty: "{selected}" ({zone}) at index {index}')
#         ZONE[0] = zone


    
#     # play_menu.add.button('Send',  # When pressing return -> play(DIFFICULTY[0], font)
#     #                      play_function,
#     #                      DIFFICULTY,
#     #                      pygame.font.Font(pygame_menu.font.FONT_FRANCHISE, 30))

# selected = "None"   
# pygame.init()
# surface = pygame.display.set_mode((600, 400))
# surface.fill((0, 0, 255))
# pygame.display.flip()
# def main_background() -> None:
#     """
#     Function used by menus, draw on background while menu is active.
#     """
#     global surface
#     surface.fill((128, 0, 128))
# def main(screen) -> None:
#     """
#     Main program.
#     :param test: Indicate function is being tested
#     """

#     # -------------------------------------------------------------------------
#     # Globals
#     # -------------------------------------------------------------------------
#     global clock
#     global main_menu
#     global surface

#     # -------------------------------------------------------------------------
#     # Create window
#     # -------------------------------------------------------------------------
#     surface = create_example_window('Example - Game Selector', WINDOW_SIZE)
#     clock = pygame.time.Clock()

#     play_menu = pygame_menu.Menu(
#         height=WINDOW_SIZE[1] * 0.7,
#         title='Play Menu',
#         width=WINDOW_SIZE[0] * 0.75
#     )
#     play_submenu = pygame_menu.Menu(
#         height=WINDOW_SIZE[1] * 0.5,
#         theme=pygame_menu.themes.THEME_BLUE,
#         title='Submenu',
#         width=WINDOW_SIZE[0] * 0.7)
#     play_menu.add.button('Return to main menu', pygame_menu.events.BACK)
    
#     play_menu.add.selector('Select zone: ',
#                            [('1 - General', 'General'),
#                             ('2 - Res', 'RES'),
#                             ('3 - Ind', 'INDs')],
#                            onchange=change_difficulty,
#                            selector_id='select_difficulty')
#     while True:

#         # Tick
#         clock.tick(FPS)

#         # Paint background
#         main_background()

#         # Application events
#         events = pygame.event.get()
#         for event in events:
#             if event.type == pygame.QUIT:
#                 exit()

#         # Main menu
#         if play_menu.is_enabled():
#             play_menu.mainloop(surface, main_background, fps_limit=FPS)

#         # Flip surface
#         pygame.display.flip()
# # menu.center_content()


