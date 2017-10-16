import random
from enum import Enum

class one_handed_sword_type(Enum):
    tiger_hook = 1
    midnight_blade = 2

class weapon():
    def __init__(self):
        self.prefix_mods = 0
        self.suffix_mods = 0
        self.attack_speed = 0.0
        self.min_dmg = 0
        self.max_dmg = 0
        self.item_level = 0
        self.crit_chance = 0.0

    def weapon_dps(self):
        return (self.min_dmg + self.max_dmg) / 2 * self.attack_speed

class one_handed_sword(weapon):
    def __init__(self, type):
        super().__init__()
        self.set_type(type)

    def set_type(self, type):
        if type == one_handed_sword_type.tiger_hook:
            self.min_dmg = 49
            self.max_dmg = 105
            self.attack_speed = 1.15
            self.crit_chance = 5.00

        elif type == one_handed_sword_type.midnight_blade:
            self.min_dmg = 35
            self.max_dmg = 99
            self.attack_speed = 1.30
            self.crit_chance = 5.00



def use_alteration(count):
    counter = 0
    for i in range(count):
        random_number = random.randrange(0, 100)
        if random_number <= 49:
            prefix = True #change to class
        else:
            suffix = True #change to class
        random_float = (random.random()) * 100
        if random_float <= 0.04 and prefix:
            counter += 1
    return counter

wep_1 = one_handed_sword(one_handed_sword_type.midnight_blade)
print(wep_1.weapon_dps())
