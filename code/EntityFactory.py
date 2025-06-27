import random

from code.Background import Background
from code.Const import WIN_WIDTH, WIN_HEIGHT
from code.Enemy import Enemy


class EntityFactory:

    @staticmethod
    def get_entity(entity_name:str, position = (0,0)):
        match entity_name:
            case 'Level1Bg':
                list_bg = []
                for i in range(4):
                    list_bg.append(Background(f'Level1Bg{i}', (0,0)))
                    list_bg.append(Background(f'Level1Bg{i}', (WIN_WIDTH, 0)))
                return list_bg
            case 'Enemy1':
                return Enemy('Enemy1', (random.randint(40, WIN_WIDTH - 40), WIN_HEIGHT + 10))
            case 'Enemy2':
                return Enemy('Enemy2', (random.randint(40, WIN_WIDTH - 40), WIN_HEIGHT + 10))
            case 'Enemy3':
                return Enemy('Enemy3', (random.randint(40, WIN_WIDTH - 40), WIN_HEIGHT + 10))

