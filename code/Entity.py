from abc import ABC, abstractmethod

import pygame.image

from code.Const import ENTITY_HEALTH, ENTITY_SCORE


class Entity(ABC):
    def __init__(self, name: str, position: tuple):
        self.name = name
        if self.name == 'Player':
            pass
        else:
            self.surf = pygame.image.load('./assets/' + name + '.png').convert_alpha()
            self.rect = self.surf.get_rect(left=position[0], top=position[1])
        self.speed = 0
        self.health = ENTITY_HEALTH[self.name]
        self.last_dmg = 'None'
        self.score = ENTITY_SCORE[self.name]

    @abstractmethod
    def move(self):
        pass