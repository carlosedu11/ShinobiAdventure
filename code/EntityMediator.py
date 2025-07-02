from code.Const import WIN_HEIGHT
from code.Enemy import Enemy
from code.Entity import Entity


class EntityMediator:

    @staticmethod
    def __verify_collision_window(ent: Entity):
        if isinstance(ent, Enemy):
            if ent.rect.top >= WIN_HEIGHT:
                ent.health = 0

    @staticmethod
    def verify_destroy(ent: Entity):
        if isinstance(ent, Enemy):
            ent.health = 0


    @staticmethod
    def verify_collision(entity_list: list[Entity]):
        for i in range(len(entity_list)):
            entity1 = entity_list[i]
            EntityMediator.__verify_collision_window(entity1)


    @staticmethod
    def verify_health(entity_list: list[Entity]):
        for ent in entity_list:
            if ent.health <= 0:
                if isinstance(ent, Enemy):
                    EntityMediator.__give_score(ent, entity_list)
                    entity_list.remove(ent)


    @staticmethod
    def __give_score(enemy: Enemy, entity_list: list[Entity]):
        for ent in entity_list:
            if ent.name == 'Player':
                ent.score += enemy.score

