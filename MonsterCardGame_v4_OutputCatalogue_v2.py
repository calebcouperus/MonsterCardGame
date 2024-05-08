import easygui

# list of all initial monster cards
monsters = {
    'Stoneling': {
        "Name": "Stoneling",
        'Strength': 7,
        'Speed': 1,
        'Stealth': 25,
        'Cunning': 15},

    'Vexscream': {
        "Name": "Vexscream",
        'Strength': 1,
        'Speed': 6,
        'Stealth': 21,
        'Cunning': 19},
    'Dawnmirage': {
        "Name": "Dawnmirage",
        'Strength': 5,
        'Speed': 15,
        'Stealth': 18,
        'Cunning': 22},
    'Blazegolem': {
        "Name": "Blazegolem",
        'Strength': 15,
        'Speed': 20,
        'Stealth': 23,
        'Cunning': 6},
    'Websnake': {
        "Name": "Websnake",
        'Strength': 7,
        'Speed': 15,
        'Stealth': 10,
        'Cunning': 5},
    'Moldvine': {
        "Name": "Moldvine",
        'Strength': 21,
        'Speed': 18,
        'Stealth': 14,
        'Cunning': 5},
    'Vortexwing': {
        "Name": "Vortexwing",
        'Strength': 19,
        'Speed': 13,
        'Stealth': 19,
        'Cunning': 2},
    'Rotthing': {
        "Name": "Rotthing",
        'Strength': 16,
        'Speed': 7,
        'Stealth': 4,
        'Cunning': 12},
    'Froststep': {
        "Name": "Froststep",
        'Strength': 14,
        'Speed': 14,
        'Stealth': 17,
        'Cunning': 4},
    'Wispghoul': {
        "Name": "Wispghoul",
        'Strength': 17,
        'Speed': 19,
        'Stealth': 3,
        'Cunning': 2},
}


def print_catalogue():
    catalogue = '***MONSTER CATALOGUE***\n\n'
    for monster_name, monster_info in monsters.items():
        catalogue += f'{monster_name}\n'
        for attribute, value in monster_info.items():
            catalogue += f' - {attribute}: {value}'
        catalogue += "\n\n"

    easygui.msgbox(catalogue, title='Catalogue')


print_catalogue()
