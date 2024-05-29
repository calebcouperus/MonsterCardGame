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


# Function for editing cards
def edit_card():
    card_names = list(monsters.keys())
    choice_edit = easygui.choicebox(msg='Select a card to edit:',
                                    choices=card_names)

    if choice_edit:
        selected_card = monsters[choice_edit]

        # Ask user to enter new values for the selected card
        new_card_values = easygui.multenterbox('Enter new values:',
                                               fields=('Monster Name:',
                                                       'Strength', 'Speed',
                                                       'Stealth', 'Cunning'),
                                               values=(selected_card['Name'],
                                                       str(selected_card[
                                                               'Strength']),
                                                       str(selected_card[
                                                               'Speed']),
                                                       str(selected_card[
                                                               'Stealth']),
                                                       str(selected_card[
                                                               'Cunning'])))

        try:
            new_strength = int(new_card_values[1])
            new_speed = int(new_card_values[2])
            new_stealth = int(new_card_values[3])
            new_cunning = int(new_card_values[4])

            if 1 <= new_strength <= 25 and 1 <= new_speed <= 25 and 1 <= \
                    new_stealth <= 25 and 1 <= new_cunning <= 25:
                selected_card['Name'] = new_card_values[0]
                selected_card['Strength'] = new_strength
                selected_card['Speed'] = new_speed
                selected_card['Stealth'] = new_stealth
                selected_card['Cunning'] = new_cunning

                easygui.msgbox('Card edited successfully!', title='Success')
            else:
                easygui.msgbox('Please enter values between 1 and 25 for'
                               ' Strength, Speed, Stealth, and Cunning.',
                               title='Error')
        except ValueError:
            easygui.msgbox('Please enter valid numerical values for Strength,'
                           ' Speed, Stealth, and Cunning.', title='Error')
        except TypeError:
            easygui.msgbox("Cancelled - Try Again", title='Cancelled')
            return None
    else:
        easygui.msgbox('No card selected.', title='Cancelled')


# Call the function to edit an existing card
edit_card()
