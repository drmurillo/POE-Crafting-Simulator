import random
from enum import Enum

class one_handed_sword_type(Enum):
    tiger_hook = 1
    midnight_blade = 2

class weapon():
    def __init__(self):
        # Name of weapon
        self.prefix_name = ''
        self.suffix_name = ''
        self.base_name = ''

        # Combat stats on the item
        self.prefix_mods = 0
        self.suffix_mods = 0
        self.attack_speed = 0.0
        self.min_dmg = 0
        self.max_dmg = 0
        self.item_level = 0
        self.crit_chance = 0.0
        # Tracking currency used on the item
        self.alt_count = 0
        self.aug_count = 0

    def __str__(self):
        # Return both prefix, base name and suffix name if item has a prefix and suffix
        if self.prefix_name is not '' and self.suffix_name is not '':
            return "{} {} of {}".format(self.prefix_name, self.base_name, self.suffix_name)
        # Returns base name and suffix name if there is no prefix name
        elif self.prefix_name == '' and self.suffix_name is not '':
            return "{} of {}".format(self.base_name, self.suffix_name)
        # Returns prefix name and base name if there is no suffix name
        elif self.prefix_name is not '' and self.suffix_name == '':
            return "{} {}".format(self.prefix_name, self.base_name)
        # Returns just the base name
        else:
            return "{}".format(self.base_name)


    @property
    def weapon_dps(self):
        return (self.min_dmg + self.max_dmg) / 2 * self.attack_speed


    def incr_alt_count_by(self, increment):
        self.alt_count += increment

    def incr_aug_count_by(self, increment):
        self.aug_count += increment

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
            self.base_name = 'Tiger Hook'

        elif type == one_handed_sword_type.midnight_blade:
            self.min_dmg = 35
            self.max_dmg = 99
            self.attack_speed = 1.30
            self.crit_chance = 5.00
            self.base_name = 'Midnight Blade'







wep_1 = one_handed_sword(one_handed_sword_type.tiger_hook)

def use_alteration(count, weapon):
    weapon_list = []
    for i in range(count):
        random_number = random.randrange(0, 100)
        weapon.prefix_mods = 0
        weapon.suffix_mods = 0
        weapon.incr_alt_count_by(1)
        # Check if both prefix and suffix are rolled (50% chance)
        if random_number <= 49:
            weapon.prefix_mods = 1
            weapon.suffix_mods = 1
        # Check if prefix is rolled (25% chance)
        if random_number <= 24 and weapon.prefix_mods == 0:
            weapon.prefix_mods = 1
        # Check if suffix is rolled (25% chance)
        elif random_number >= 75 and weapon.suffix_mods == 0:
            weapon.suffix_mods = 1
            if weapon.prefix_mods == 0:
                weapon.incr_aug_count_by(1)
                weapon.prefix_mods = 1
        random_float = (random.random()) * 100
        if random_float <= 0.04 and weapon.prefix_mods == 1:
            weapon.prefix_name = 'Merciless'
            finished_weapon = weapon
            weapon_list.append(finished_weapon)

    return weapon_list

t1_phys_wep_list = use_alteration(2500, wep_1)


for i in range(len(t1_phys_wep_list)):
    print(t1_phys_wep_list[i].alt_count)
    print(t1_phys_wep_list[i].aug_count)