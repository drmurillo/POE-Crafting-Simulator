import random
from weapons import *


def assign_prefix(item):
    if item.prefix_mods == 1:
        random_float = (random.random()) * 100
        item.prefix_list(random_float)
        return item

    elif item.prefix_mods == 2:
        pass
    elif item.prefix_mods == 3:
        pass
    else:
        return item


def assign_suffix(item):
    if item.suffix_mods == 1:
        random_float = (random.random()) * 100
        item.suffix_list(random_float)
        return item

    elif item.suffix_mods == 2:
        pass
    elif item.suffix_mods == 3:
        pass
    else:
        return item


def use_alteration(item):
    random_number = random.randrange(0, 100)
    item.incr_alt_count_by(1)
    # Check if both prefix and suffix are rolled (40% chance)
    if random_number <= 39:
        item.prefix_mods = 1
        assign_prefix(item)
        item.suffix_mods = 1
        assign_suffix(item)
    # Check if prefix is rolled (30% chance)
    if 40 <= random_number <= 70 and item.prefix_mods == 0:
        item.prefix_mods = 1
        assign_prefix(item)
    # Check if suffix is rolled (30% chance)
    elif 71 <= random_number <= 100 and item.suffix_mods == 0:
        item.suffix_mods = 1
        assign_suffix(item)
        #if item.prefix_mods == 0:
            #item.incr_aug_count_by(1)
            #item.prefix_mods = 1
    return item

wep_1 = one_handed_sword(one_handed_sword_type.tiger_hook)

weapon_list = []

for i in range(2500):
    use_alteration(wep_1)
    if wep_1.prefix_name == 'T1 Dictator\'s':
        weapon_list.append(wep_1)
        wep_1 = one_handed_sword(one_handed_sword_type.tiger_hook)
for i in range(len(weapon_list)):
    print("Weapon: {}'s alt count: {}".format(weapon_list[i], weapon_list[i].alt_count))


