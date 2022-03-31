ITEM_TYPES = ['weapon', 'armor', 'potion', 'special']

class Item():

    def __init__(self, name, description, type):
        self.name = name
        self.description = description
        self.type = type

class WoodenStick(Item):

    def __init__(self):
        super().__init__(name="Wooden Stick", description="A small wooden stick.", type="weapon")
        self.damage = 30

    def attack_enemy(self, enemy):
        enemy.health -= self.damage
        return self.damage