import pygame

from code.Const import WIN_HEIGHT, WIN_WIDTH, MENU_OPTION
from code.Menu import Menu
from code.Level import Level
from code.Score import Score


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))

    def run(self):
        while True:
            score = Score(self.window)
            menu = Menu(self.window)
            option_chosen = menu.run()

            if option_chosen in [MENU_OPTION[0]]:
                player_score = [0]
                level = Level(self.window,'Level1', option_chosen, player_score)
                level_return = level.run(player_score)
                if level_return:
                    level = Level(self.window, 'Level2', option_chosen, player_score)
                    level_return = level.run(player_score)
                    if level_return:
                        score.save(option_chosen, player_score)

            elif option_chosen == MENU_OPTION[1]:
                score.show()
            elif option_chosen == MENU_OPTION[2]:
                pygame.quit() #Close Window
                quit() #End Pygame
            else:
                pass





