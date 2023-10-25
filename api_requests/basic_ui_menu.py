from prettytable import PrettyTable

def menu_table():
    option_number = 1
    option_list = ['Lookup a destination', 'View bookmarks', 'Quit']
    menu_table = PrettyTable(['Number', 'Option'])
    for i in option_list:
        menu_table.add_row([option_number, i])
        option_number = option_number + 1
    return menu_table

def user_selection():
    selection = input('What would you like to do? Enter a number: ')
    return selection