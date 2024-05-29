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


# Function for adding cards
def add_card():
    while True:
        # asks user to enter values for new card
        new_card_values = easygui.multenterbox(msg='Enter Valid info:',
                                               fields=(
                                                   'Monster Name:', 'Strength',
                                                   'Speed', 'stealth',
                                                   'cunning'),
                                               values=())
        # attempts to convert values making sure they are correct types to
        # match other cards
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
                    # Confirmation for adding card and user checks card
                    # details entered are correct
                    monsters[f"{card_name}"] = new_card
                    add_confirmation = easygui.buttonbox(
                        f'Is this what you want on the new '
                        f'card:\n'
                        f'{new_card}', choices=('Yes', 'No'),
                        title='Add Confirmation')
                    if add_confirmation == 'Yes':
                        easygui.msgbox("New Card has been successfully added")
                        break
                except ValueError:
                    easygui.msgbox('Please enter Strength, Speed, Stealth, '
                                   'and Cunning as integers from 1 - 25.')
            else:
                easygui.msgbox('Please enter Strength, Speed, Stealth, '
                               'and Cunning as integers from 1 - 25.')
        # Avoid errors from crashing program just warns user to enter correct
        # inputs
        except TypeError:
            return None

        except (ValueError, IndexError):
            easygui.msgbox('Please enter Strength, Speed, Stealth, '
                           'and Cunning as integers from 1 - 25.')


# Function to format card to look good
def format_monster_card(monster_name, monster_info):
    formatted_card = f" **Monster Card - {monster_name}** \n\n"
    for key, value in monster_info.items():
        formatted_card += f"{key}: {value}\n"
    return formatted_card


# Function to be called for main search function
def search_card(search_name):
    for monster_name, monster_info in monsters.items():
        if search_name.lower() in monster_name.lower():
            return monster_info
    return None


# Function for the delete search returns different to other search function
# as the delete function needs monster_name and monster_info
def search_card_delete(search_name):
    for monster_name, monster_info in monsters.items():
        if search_name.lower() in monster_name.lower():
            return monster_name, monster_info
    return None


# Main search function
def search():
    search_term = easygui.enterbox("Enter the name of the monster you want to "
                                   "search for:", title='Search')
    # calls searching function
    result = search_card(search_term)

    # if and else to make sure search is in the catalogue
    if result:
        formatted_result = format_monster_card(search_term, result)
        easygui.msgbox(formatted_result, "Monster Card")
    else:
        easygui.msgbox("Monster not found in catalogue.", "Search Result")


# function for deleting cards
def delete_monster():
    search_term = easygui.enterbox(
        "Enter the name of the monster card you want to delete:",
        title='Enter Search')
    search_result = search_card_delete(search_term)

    # confirmation for delete
    if search_result:
        monster_name, monster_info = search_result
        confirm = easygui.boolbox(
            f"Are you sure you want to delete the Monster Card '"
            f"{monster_name}?\n"
            f"{format_monster_card(monster_name, monster_info)}'",
            title='Confirmation', choices=("Yes", "No"))

        # actually deleting
        if confirm:
            del monsters[monster_name]
            easygui.msgbox(f"Monster '{monster_name}' has been deleted.",
                           "Deletion Successful")
        # if deletion is cancelled by user
        else:
            easygui.msgbox("Deletion canceled.", "Deletion Canceled")
    # If deletion is cancelled because users search didn't return a card
    else:
        easygui.msgbox("Monster not found in catalogue.", "Deletion Failed")


# Function to print whole catalogue
def print_catalogue():
    # Spaces to centre main title
    catalogue = '                               ***MONSTER CATALOGUE***\n\n'
    for monster_name, monster_info in monsters.items():
        catalogue += f'{monster_name}\n'
        for attribute, value in monster_info.items():
            catalogue += f' - {attribute}: {value}'
        catalogue += "\n\n"

    easygui.msgbox(catalogue, title='Catalogue')


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


# main loop
while True:
    # Main UI
    choice = easygui.buttonbox("Welcome to the Monster Cards Catalogue\n"
                               "       What would you like to do:",
                               title='Main Screen',
                               choices=(
                                   "Add a Card",
                                   "Search for a Card",
                                   "Edit a Card",
                                   "Delete a Card",
                                   "View the Catalogue",
                                   "Exit"))
    if choice == "Add a Card":
        add_card()

    elif choice == "Search for a Card":
        search()

    elif choice == "Delete a Card":
        delete_monster()

    elif choice == "View the Catalogue":
        print_catalogue()

    elif choice == "Edit a Card":
        edit_card()

    # Breaks loop if user selects 'Exit' or the program throws a tantrum
    else:
        break

# Final goodbye message
easygui.msgbox("Goodbye")
