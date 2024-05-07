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


def format_monster_card(monster_name, monster_info):
    formatted_card = f" **Monster Card - {monster_name}** \n\n"
    for key, value in monster_info.items():
        formatted_card += f"{key}: {value}\n"
    return formatted_card


def search_card(search_name):
    for monster_name, monster_info in monsters.items():
        if search_name.lower() in monster_name.lower():
            return monster_name, monster_info
    return None


def search():
    search_term = easygui.enterbox("Enter the name of the monster you want to "
                                   "search for:", title='End Search')
    result = search_card(search_term)

    if result:
        formatted_result = format_monster_card(search_term, result)
        easygui.msgbox(formatted_result, "Monster Card")
    else:
        easygui.msgbox("Monster not found in catalogue.", "Search Result")


def delete_monster():
    search_term = easygui.enterbox(
        "Enter the name of the monster card you want to delete:",
        title='Enter Search')
    search_result = search_card(search_term)

    if search_result:
        monster_name, monster_info = search_result
        confirm = easygui.boolbox(
            f"Are you sure you want to delete the Monster Card '{monster_name}'?",
            title='Confirmation', choices=("Yes", "No"))

        if confirm:
            del monsters[monster_name]
            easygui.msgbox(f"Monster '{monster_name}' has been deleted.",
                           "Deletion Successful")
        else:
            easygui.msgbox("Deletion canceled.", "Deletion Canceled")
    else:
        easygui.msgbox("Monster not found in catalogue.", "Deletion Failed")


delete_monster()
