import random
from enum import Enum
from modList import prefix_list


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

    def __repr__(self):
        return str(self)

    @property
    def weapon_dps(self):
        return (self.min_dmg + self.max_dmg) / 2 * self.attack_speed

    @property
    def mod_list(self, mod):
        mod_list = [mod]
        return mod_list

    def clear_mods(self):
        self.prefix_name = ''
        self.suffix_name = ''
        self.prefix_mods = 0
        self.suffix_mods = 0
        self.alt_count = 0
        self.aug_count = 0

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


def assign_prefix(item):
    #print("assign_prefix Item: {}".format(item))
    #print("Prefix: {} Suffix: {}".format(item.prefix_mods, item.suffix_mods))
    if item.prefix_mods == 1:
        random_float = (random.random()) * 100
        #print(random_float)
        item.prefix_name = prefix_list(random_float)
        #print("Prefix name: {}".format(item.prefix_name))
        return item

    elif item.prefix_mods == 2:
        pass
    elif item.prefix_mods == 3:
        pass
    else:
        return item


def use_alteration(item):
    #print("Item coming into function {}".format(item))

    random_number = random.randrange(0, 100)
    item.incr_alt_count_by(1)
    # Check if both prefix and suffix are rolled (40% chance)
    if random_number <= 39:
        item.prefix_mods = 1
        item.suffix_mods = 1
    # Check if prefix is rolled (30% chance)
    if 40 <= random_number <= 70 and item.prefix_mods == 0:
        item.prefix_mods = 1
    # Check if suffix is rolled (30% chance)
    elif 71 <= random_number <= 100 and item.suffix_mods == 0:
        item.suffix_mods = 1
        if item.prefix_mods == 0:
            item.incr_aug_count_by(1)
            item.prefix_mods = 1

    return assign_prefix(item)

wep_1 = one_handed_sword(one_handed_sword_type.tiger_hook)
weapon_list = []
for i in range(5):
    use_alteration(wep_1)
    print(wep_1)
    weapon_list.append(wep_1)

print(weapon_list)

