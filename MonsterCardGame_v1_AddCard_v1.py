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


# Function for adding cards lower and upper bounds for min and max of 1 and
# 25, looped to allow for a confirmation  message for the user to make sure
# they have entered what they want to correctly.
def add_card():
    while True:
        name = easygui.enterbox(
            "Enter the Monsters name for the new card:",
            title='Enter Monster Name')
        strength = easygui.integerbox(
            "Enter the strength of the monster on the new card:",
            title='Enter Strength', lowerbound=1, upperbound=25)
        speed = easygui.integerbox(
            "Enter the speed of the monster on the new card:",
            title='Enter Speed', lowerbound=1, upperbound=25)
        stealth = easygui.integerbox(
            "Enter the stealth of the monster on the new card:",
            title='Enter Stealth', lowerbound=1, upperbound=25)
        cunning = easygui.integerbox(
            "Enter the cunning of the monster on the new "
            "card:",
            title='Enter Cunning', lowerbound=1, upperbound=25)
        card_name = name
        new_card = {
            'name': name,
            'strength': strength,
            'Speed': speed,
            'Stealth': stealth,
            'Cunning': cunning
        }
        monsters[f"{card_name}"] = new_card
        add_confirmation = easygui.buttonbox(
            f'Is this what you want on the new '
            f'card:\n'
            f'{new_card}', choices=('Yes', 'No'), title='Add '
                                                        'Confirmation')
        if add_confirmation == 'Yes':
            break


# main, for testing purposes only
add_card()
print(monsters)
