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
        inputs = ui.get_inputs(["Please enter a number: "], "")
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

    # your code

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
    max_ids = []
    for row in table:
        for i in longest_names:
            if i in longest_names and i in row:
                max_ids.append(row[0])
    label = "ID of customers with longest names"
    ui.print_result(max_ids, label)
    return max_ids
#get_longest_name_id('customers.csv')
# the question: Which customers have subscribed to the newsletter?
# return type: list of string (where string is like email+separator+name, separator=";")


def get_subscribed_emails(table):
    table = data_manager.get_table_from_file(current_file_path + '/customers.csv')
    title_list = "Subscribers"
    with open('customers.csv', "r") as file:
        lines = file.readlines()
    table = [element.replace("\n", "").split(";") for element in lines]
    subscribed = []
    for i in table:
        if int(i[3]) == 1:
            subscribed.append("{0};{1}".format(i[2], i[1]))
    label = "Subscribed Customers"
    ui.print_result(subscribed, label)
    return subscribed
#get_subscribed_emails('customers.csv')
