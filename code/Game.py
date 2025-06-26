import pygame

from code.Const import WIN_HEIGHT, WIN_WIDTH, MENU_OPTION
from code.Menu import Menu
from code.Level import Level


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))

    def run(self):
        while True:
            menu = Menu(self.window)
            option_chosen = menu.run()

            if option_chosen in [MENU_OPTION[0], MENU_OPTION[1], MENU_OPTION[2]] :
                level = Level(self.window,'Level1', option_chosen)
                level_return = level.run()
            elif option_chosen == MENU_OPTION[4]:
                pygame.quit() #Close Window
                quit() #End Pygame
            else:
                pass





