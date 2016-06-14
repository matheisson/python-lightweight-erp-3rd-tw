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

def start_module():
    list_options = ["Show table", "Add new item", "Remove item", "Update item",
                    "ID with the longest name", "Subscribers", "Exit"]
    while True:
        ui.print_menu("CRM Menu", list_options, "Back to Main")
        inputs = ui.get_inputs(["Please enter a number"], "")
        option = inputs[0]
        table = table.get_table_from_file('customers.csv')
        if option == "1":
            show_table()
        elif option == "2":
            add()
        elif option == "3":
            remove()
        elif option == "4":
            update()
        elif option == "5":
            get_longest_name_id()
        elif option == "6":
            get_subscribed_emails()
        elif option == "0":
            sys.exit(0)
        else:
            raise KeyError("There is no such option.")
# print the default table of records from the file

# @table: list of lists
#


def show_table(table):
    ui.print_table(table, ["ID", "NAME", "EMAIL", "SUBSCRIBED"])

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
    data = data_manager.get_table_from_file('customers.csv')
    names = [str(i[1]) for i in table]
    ids = [str(i[0]) for i in table]
    top_names = max(names, key=len)  # the longest name
    for names in table:
        if top_names in names:
            top_ids = table[0][0]  # id of the longest name
        else:
            continue
    ui.print_table(top_ids)  # Most csak egyet ír ki, de több van! Mi a frászt csináljak???

    return(top_ids)

# the question: Which customers have subscribed to the newsletter?
# return type: list of string (where string is like email+separator+name, separator=";")


def get_subscribed_emails(table):
    # data = table
    with open('customers.csv', "r") as file:
        lines = file.readlines()
    table = [element.replace("\n", "").split(";") for element in lines]
    subscribed = []
    for i in table:
        if int(i[3]) == 1:
            subscribed.append("{0};{1}".format(i[2], i[1]))

    ui.print_table(subscribed)

    return subscribed
