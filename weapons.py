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
            return "{} {} {}".format(self.prefix_name, self.base_name, self.suffix_name)
        # Returns base name and suffix name if there is no prefix name
        elif self.prefix_name == '' and self.suffix_name is not '':
            return "{} {}".format(self.base_name, self.suffix_name)
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

    def prefix_list(self, num):
        # #% increased Physical Damage, # to Accuracy Rating
        if num <= 1.85:
            self.prefix_name = "T8 Squire\'s"
        if 1.86 <= num <= 3.71:
            self.prefix_name = "T7 Journeyman\'s"
        if 3.72 <= num <= 5.57:
            self.prefix_name = "T6 Reaver\'s"
        if 5.58 <= num <= 6.32:
            self.prefix_name = "T5 Mercenary\'s"
        if 6.33 <= num <= 6.70:
            self.prefix_name = "T4 Champion\'s"
        if 6.71 <= num <= 6.90:
            self.prefix_name = "T3 Conqueror\'s"
        if 6.91 <= num <= 7.00:
            self.prefix_name = "T2 Emperor\'s"
        if 7.01 <= num <= 7.06:
            self.prefix_name = "T1 Dictator\'s"

    def suffix_list(self, num):
        # # to Strength
        if num <= 1.04:
            self.suffix_name = "T9 of the Brute"
        if 1.05 <= num <= 2.09:
            self.suffix_name = "T8 of the Wrestler"
        if 2.10 <= num <= 3.14:
            self.suffix_name = "T7 of the Bear"
        if 3.15 <= num <= 4.19:
            self.suffix_name = "T6 of the Lion"
        if 4.20 <= num <= 5.24:
            self.suffix_name = "T5 of the Gorilla"
        if 5.25 <= num <= 6.29:
            self.suffix_name = "T4 of the Goliath"
        if 6.30 <= num <= 7.34:
            self.suffix_name = "T3 of the Leviathan"
        if 7.35 <= num <= 8.39:
            self.suffix_name = "T2 of the Titan"
        if 8.40 <= num <= 9.44:
            self.suffix_name = "T1 of the Gods"
