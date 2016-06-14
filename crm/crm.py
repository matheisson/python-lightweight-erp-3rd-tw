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
title = 'Customer relationship management (CRM)'

def start_module():
    file_name = 'customers.csv'
    table = data_manager.get_table_from_file(file_name)
    options = ["Show Table",
               "Add new data",
               "Remove data",
               "Update a record",
               "Longest name",
               "Subscriptions"]

    crm_menu = ui.print_menu("Main Menu", options, "Exit program")

    inputs = ui.get_inputs(["Please enter a number: "], "")
    option = inputs[0]
    if option == "1":
        crm.show_table()
    elif option == "2":
        crm.add()
    elif option == "3":
        crm.remove()
    elif option == "4":
        crm.update()
    elif option == "5":
        crm.get_longest_name_id()
    elif option == "6":
        crm.get_subscribed_emails()
    elif option == "0":
        sys.exit(0)
    else:
        raise KeyError("There is no such option.")


# print the default table of records from the file
#
# @table: list of lists
def show_table(table):
    option = data_manager.get_table_from

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
    data = []
    with open("customers.csv") as f:
        readCSV = csv.reader(inputfile, delimiter='\t')
        for row in readCSV:
           data.append(''.join(row))
        print(data)
get_longest_name_id('customers.csv')


# the question: Which customers have subscribed to the newsletter?
# return type: list of string (where string is like email+separator+name, separator=";")
def get_subscribed_emails(table):
    subscribers = []
