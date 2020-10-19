def append_with_comma(a, b):
    return str(a) + ", " + str(b)


def get_main_category(value):
    main_categories = {
        1: "Main Weapon",
        5: "Sub-Weapon",
        10: "Awakening",
        15: "Armor",
        20: "Accessories",
        25: "Material",
        30: "Enhancement/Upgrade",
        35: "Consumables",
        40: "Life Tools",
        45: "Alchemy Stones",
        50: "Magic Crystal",
        55: "Pearl Item",
        60: "Dye",
        65: "Mount",
        70: "Ship",
        75: "Wagon",
        80: "Furniture"
    }
    return main_categories.get(value, "N/A")

def get_subcategory(value1, value2):
    sub_categories = {
        1: {
            1: "Longsword", 
            2: "Longbow", 
            3: "Amulet", 
            4: "Axe", 
            5: "Shortsword", 
            6: "Blade", 
            7: "Staff", 
            8: "Kriegsmesser", 
            9: "Gauntlet", 
            10: "Crescent Pendulum", 
            11: "Crossbow", 
            12: "Florang", 
            13: "Battle Axe"
            },
        5: {
            1: "Shield", 
            2: "Dagger", 
            3: "Talisman", 
            4: "Ornamental Knot", 
            5: "Trinket", 
            6: "Horn Bow", 
            7: "Kunai", 
            8: "Shuriken", 
            9: "Vanbrace", 
            10: "Noble Sword", 
            11: "Ra'ghon", 
            12: "Vitclari"
            },
        10: {
            1: "Great Sword", 
            2: "Scythe", 
            3: "Iron Buster", 
            4: "Kamasylven Sword", 
            5: "Celestial Bo Staff", 
            6: "Lancia", 
            7: "Crescent Blade", 
            8: "Kerispear", 
            9: "Sura Katana", 
            10: "Sah Chakram", 
            11: "Aad Spera", 
            12: "Godr Sphera", 
            13: "Vediant", 
            14: "Gardbrace", 
            15: "Cestus", 
            16: "Crimson Glaives", 
            17: "Greatbow", 
            18: "Jordun"},
        15: {
            1: "Helmet", 
            2: "Armor", 
            3: "Gloves", 
            4: "Shoes", 
            5: "Functional Clothes", 
            6: "Crafted Clothes"},
        20: {
            1: "Ring", 
            2: "Necklace", 
            3: "Earring", 
            4: "Belt"},
        25: {
            1: "Ore/Gem", 
            2: "Plants", 
            3: "Seed/Fruit", 
            4: "Leather", 
            5: "Blood", 
            6: "Meat", 
            7: "Seafood", 
            8: "Misc."},
        30: {
            1: "Blackstone", 
            2: "Upgrade"},
        35: {
            1: "Offensive Elixir", 
            2: "Defensive Elixir", 
            3: "Functional Elixir", 
            4: "Food", 
            5: "Potion", 
            6: "Siege Items", 
            7: "Item Parts", 
            8: "Other Consumables"},
        40: {
            1: "Lumbering Axe", 
            2: "Fluid Collector", 
            3: "Butcher Knife", 
            4: "Pickaxe", 
            5: "Hoe", 
            6: "Tanning Knife", 
            7: "Fishing Tools", 
            8: "Matchlock", 
            9: "Alchemy/Cooking", 
            10: "Other Tools"},
        45: {
            1: "Destruction", 
            2: "Protection", 
            3: "Life", 
            4: "Spirit Stone"},
        50: {
            1: "Main Weapon", 
            2: "Sub-weapon", 
            3: "Helmet", 
            4: "Armor", 
            5: "Gloves", 
            6: "Shoes", 
            7: "Versatile"},
        55: {
            1: "Male Apparel (Set)", 
            2: "Female Apparels (Set)", 
            3: "Male Apparel (Individual)", 
            4: "Female Apparel (Individual)", 
            5: "Class-based Apparel (Set)", 
            6: "Functional", 
            7: "Mount", 
            8: "Pet"},
        60: {
            1: "Basic", 
            2: "Olvia", 
            3: "Velia", 
            4: "Heidelian", 
            5: "Keplan", 
            6: "Calpheon", 
            7: "Mediah", 
            8: "Valencia"},
        65: {
            1: "Registration", 
            2: "Feed", 
            3: "Champron", 
            4: "Barding", 
            5: "Saddle", 
            6: "Stirrups", 
            7: "Horseshoe", 
            8: "[Elephant] Stirrups", 
            9: "[Elephant] Armor", 
            10: "[Elephant] Mask", 
            11: "[Elephant] Saddle", 
            12: "Courser Training"},
        70: {
            1: "Registration", 
            2: "Cargo", 
            3: "Prow", 
            4: "Decoration", 
            5: "Totem", 
            6: "Prow Statue", 
            7: "Plating", 
            8: "Cannon", 
            9: "Sail"},
        75: {
            1: "Registration", 
            2: "Wheel", 
            3: "Cover", 
            4: "Flag", 
            5: "Emblem", 
            6: "Lamp"},
        80: {
            1: "Bed", 
            2: "Bedside Table/Table", 
            3: "Wardrobe/Bookshelf", 
            4: "Sofa/Chair", 
            5: "Chandelier", 
            6: "Floor/Carpet", 
            7: "Wall/Curtain", 
            8: "Decoration", 
            9: "Others"}
    }
    return sub_categories.get(value1, {}).get(value2, "N/A")

def get_enhancement(value):
    levels = {
        0: "+0",
        1: "+1",
        2: "+2",
        3: "+3",
        4: "+4",
        5: "+5",
        6: "+6",
        7: "+7",
        8: "+8",
        9: "+9",
        10: "+10",
        11: "+11",
        12: "+12",
        13: "+13",
        14: "+14",
        15: "+15",
        16: "PRI",
        17: "DUO",
        18: "TRI",
        19: "TET",
        20: "PEN",
    }
    return levels.get(value, "N/A")

def get_grade(value):
    grades = {
        1: "Normal",
        2: "Magic",
        3: "Rare",
        4: "Legendary"
    }
    return grades.get(value, "N/A")

# Print iterations progress
def print_progress_bar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█', printEnd = "\r"):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
        printEnd    - Optional  : end character (e.g. "\r", "\r\n") (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end = printEnd)
    # Print New Line on Complete
    if iteration == total: 
        print()
