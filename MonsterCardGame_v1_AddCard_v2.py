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


# Function for adding cards first try is to  for min and max of 1 and
# 25, looped to allow for a confirmation  message for the user to make sure
# they have entered what they want too correctly.
def add_card():
    while True:
        new_card_values = easygui.multenterbox(msg='Enter Valid info:',
                                               fields=(
                                                   'Monster Name:', 'Strength',
                                                   'Speed', 'stealth',
                                                   'cunning'),
                                               values=())

        try:
            card_name = new_card_values[0]
            new_strength = int(new_card_values[1])
            new_speed = int(new_card_values[2])
            new_stealth = int(new_card_values[3])
            new_cunning = int(new_card_values[4])
            if 1 <= new_strength <= 25 and 1 <= new_speed <= 25 and 1 <= \
                    new_stealth <= 25 and 1 <= new_cunning <= 25:
                try:
                    new_card = {
                        'name': new_card_values[0],
                        'strength': new_strength,
                        'Speed': new_speed,
                        'Stealth': new_stealth,
                        'Cunning': new_cunning
                    }
                    monsters[f"{card_name}"] = new_card
                    add_confirmation = easygui.buttonbox(
                        f'Is this what you want on the new '
                        f'card:\n'
                        f'{new_card}', choices=('Yes', 'No'), title='Add '
                                                                    'Confir'
                                                                    'mation')
                    if add_confirmation == 'Yes':
                        break
                except ValueError:
                    easygui.msgbox('Please enter Strength, Speed, Stealth, '
                                   'and Cunning as integers from 1 - 25.')
        except ValueError:
            easygui.msgbox('Please enter Strength, Speed, Stealth, '
                           'and Cunning as integers from 1 - 25.')


# main, for testing purposes only
add_card()
print(monsters)
