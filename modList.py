def prefix_list(num):
    # #to maximum Mana
    if num <= 1.50:
        return "(T12) Beryl"
    if 1.51 <= num <= 3.02:
        return "(T11) Cobalt"
    if 3.03 <= num <= 4.54:
        return "(T10) Azure"
    if 4.55 <= num <= 6.06:
        return "(T9) Sapphire"
    if 6.07 <= num <= 7.58:
        return "(T8) Cerulean"
    if 7.59 <= num <= 9.1:
        return "(T7) Aqua"
    if 9.11 <= num <= 10.62:
        return "(T6) Opalescent"
    if 10.63 <= num <= 12.14:
        return "(T5) Gentian"
    if 12.15 <= num <= 13.66:
        return "(T4) Chalybeous"
    if 13.67 <= num <= 15.18:
        return "(T3) Mazarine"
    if 15.19 <= num <= 16.7:
        return "(T2) Blue"
    if 16.71 <= num <= 18.22:
        return "(T1) Zaffre"
    if 18.23 <= num <= 100:
        return "(T0) Catch"
    else:
        return ""

