# data structure:
# id: string
#     Unique and random generated (at least 2 special char()expect: ';'), 2 number, 2 lower and 2 upper case letter)
# name: string
# email: string
# subscribed: boolean (Is she/he subscribed to the newsletter? 1/0 = yes/not)


# importing everything you need
import os
import csv
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
#

def get_table():
    return data_manager.get_table_from_file(current_file_path + "/customers.csv")


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
        get_longest_name_id(table)
    elif option == "6":
        get_subscribed_emails(table)
    elif option == "0":
        return "break"
    else:
        raise KeyError("There is no such option.")


def start_module():
    title = "Customer Relations Manager"
    list_options = ["Show Table", "Add to Table", "Remove from Table", "Update Element", "IDs of the longest names",
                    "Subscribers"]
    exit_message = "Back to Main Menu"
    table = get_table()
    while True:
        ui.print_menu(title, list_options, exit_message)
        try:
            valid = choose_function(table)
            if valid == "break":
                break
        except KeyError as err:
            ui.print_error_message(err)

# print the default table of records from the file

# @table: list of lists
#


def show_table(table):
    title_list = ["ID", "Name", "Email", "Subscribed(yes=1/no=0)"]
    show_tbl = ui.print_table(table, title_list)
    return table
# Ask a new record as an input from the user than add it to @table, than return @table
#
# @table: list of lists


def add(table):
    title_list = ["Name", "E-mail", "Subscribed (1/0)"]
    common.add_to_table(table, title_list)
    return table


# Remove the record having the id @id_ from the @list, than return @table
#
# @table: list of lists
# @id_: string
def remove(table, id_):

    # your code

    return table


# Update the record in @table having the id @id_ by asking the new data from the user,
# than return @table
#
# @table: list of lists
# @id_: string
def update(table, id_):

    # your code

    return table


# special functions:
# ------------------


# the question: What is the id of the customer with the longest name ?
# return type: string (id) - if there are more than one longest name, return the first of descending alphabetical order
def get_longest_name_id(table):
    table = data_manager.get_table_from_file(current_file_path + '/customers.csv')
    title_list = "IDs"
    names = [str(i[1]) for i in table]
    max_names = max(len(i) for i in names)  # how long is the longest name
    longest_names = [i for i in names if len(i) == max_names]  # customers with the longest names
    top_name = min(longest_names)
    max_id = []
    for row in table:
        if top_name in row:
            max_id.append(row[0])
    label = "ID of customers with longest names"
    ui.print_result(max_id, label)

    return max_id

# the question: Which customers have subscribed to the newsletter?
# return type: list of string (where string is like email+separator+name, separator=";")


def get_subscribed_emails(table):
    table = data_manager.get_table_from_file(current_file_path + '/customers.csv')
    title_list = "Subscribers"
    subscribed = []
    for i in table:
        if int(i[3]) == 1:
            subscribed.append("{0};{1}".format(i[2], i[1]))
    label = "Subscribed Customers"
    ui.print_result(subscribed, label)
    return subscribed
