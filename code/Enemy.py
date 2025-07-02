from code.Const import ENTITY_SPEED, WIN_HEIGHT
from code.Entity import Entity


class Enemy(Entity):
    def __init__(self, name: str, postion: tuple):
        super().__init__(name, postion)

    def move(self):
        self.rect.centery += ENTITY_SPEED[self.name]
        #if self.rect.top >= WIN_HEIGHT:
           # self.rect.bottom = 0
