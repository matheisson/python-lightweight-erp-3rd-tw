# data structure:
# id: string
#     Unique and random generated (at least 2 special char()expect: ';'), 2 number, 2 lower and 2 upper case letter)
# title: string
# manufacturer: string
# price: number (dollar)
# in_stock: number


# importing everything you need
import os
from importlib.machinery import SourceFileLoader
current_file_path = os.path.dirname(os.path.abspath(__file__))
# User interface module
ui = SourceFileLoader("ui", current_file_path + "/../ui.py").load_module()
# data manager module
data_manager = SourceFileLoader("data_manager", current_file_path + "/../data_manager.py").load_module()
# common module
common = SourceFileLoader("common", current_file_path + "/../common.py").load_module()


# start this module by a module menu like the main menu
# user need to go back to the main menu from here
# we need to reach the default and the special functions of this module from the module menu

def get_table():
    return data_manager.get_table_from_file(current_file_path + "/games.csv")


def send_table(table):
    data_manager.write_table_to_file(current_file_path + "/games.csv", table)


def choose_function(table):
    inputs = ui.get_inputs(["Choose menu: "], "")
    option = inputs[0]
    id_ = 0
    year = 0
    if option == "1":
        show_table(table)
    elif option == "2":
        add(table)
    elif option == "3":
        remove(table, id_)
    elif option == "4":
        update(table, id_)
    elif option == "5":
        get_counts_by_manufacturers(table)
    elif option == "6":
        manufacturer = get_manufacturer()
        result = get_average_by_manufacturer(table, manufacturer)
        ui.print_result(result, "")
    elif option == "0":
        return "break"
    else:
        raise KeyError("There is no such option.")


def get_manufacturer():
    Label = ["Manufacturer"]
    title = "Enter the name of the Manufacturer: "
    manufacturer = ui.get_inputs(Label, title)
    return str(manufacturer[0])


def start_module():
    title = "Store Manager"
    list_options = ["Show Table", "Add to Table", "Remove from Table", "Update Element", "Game count by Manufacturer",
                    "Average amount of games by Manufacturer"]
    exit_message = "Back to Main Menu"
    table = get_table()
    while True:
        send_table(table)
        ui.print_menu(title, list_options, exit_message)
        try:
            valid = choose_function(table)
            if valid == "break":
                break
        except KeyError as err:
            ui.print_error_message(err)


# print the default table of records from the file
#
# @table: list of lists
def show_table(table):
    title_list = ["ID", "Name", "Manufacturer", "Price (in $)", "Amount in stock"]
    show_tbl = ui.print_table(table, title_list)
    return table


# Ask a new record as an input from the user than add it to @table, than return @table
#
# @table: list of lists
def add(table):
    title_list = ["Name", "Manufacturer", "Price (in $)", "Amount in stock"]
    common.add_to_table(table, title_list)
    return table


# Remove the record having the id @id_ from the @list, than return @table
#
# @table: list of lists
# @id_: string
def remove(table, id_):
    id_ = common.get_id()
    common.remove_table(table, id_)
    return table


# Update the record in @table having the id @id_ by asking the new data from the user,
# than return @table
#
# @table: list of lists
# @id_: string
def update(table, id_):
    id_ = common.get_id()
    list_labels = ["Name", "Manufacturer", "Price (in $)", "Amount in stock"]
    title = "Update record"
    rec_upd = ui.get_inputs(list_labels, title)
    common.update_table(table, id_, rec_upd)
    return table


# special functions:
# ------------------

# the question: How many different kinds of game are available of each manufacturer?
# return type: a dictionary with this structure: { [manufacturer] : [count] }
def get_counts_by_manufacturers(table):
    games_by_manufacturer = {}
    for i in range(len(table)):
        if table[i][2] not in games_by_manufacturer:
            games_by_manufacturer[table[i][2]] = 1
        elif table[i][2] in games_by_manufacturer:
            games_by_manufacturer[table[i][2]] += 1
    return games_by_manufacturer


# the question: What is the average amount of games in stock of a given manufacturer?
# return type: number
def get_average_by_manufacturer(table, manufacturer):
    number_of_games = 0
    total_games = 0
    result = 0
    try:
        for i in range(len(table)):
            if table[i][2] == manufacturer:
                number_of_games += 1
                total_games += int(table[i][4])
        result = total_games / number_of_games
    except ZeroDivisionError:
        msg = "Manufacturer has no games in the store."
        ui.print_error_message(msg)
    return result
