# data structure:
# id: string
#     Unique and random generated (at least 2 special char()expect: ';'), 2 number, 2 lower and 2 upper case letter)
# month: number
# day: number
# year: number
# type: string (in = income, out = outcome)
# amount: number (dollar)


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


def get_table():
    return data_manager.get_table_from_file(current_file_path + "/items.csv")


def choose_function(table):
    inputs = ui.get_inputs(["Choose menu"], "")
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
        which_year_max(table)
    elif option == "6":
        avg_amount(table, year)
    elif option == "0":
        return "break"
    else:
        raise KeyError("There is no such option.")

# start this module by a module menu like the main menu
# user need to go back to the main menu from here
# we need to reach the default and the special functions of this module from the module menu


def start_module():
    title = "Accounting Manager"
    list_options = ["Show Table", "Add to Table", "Remove from Table", "Update Element", "Highest Profit",
                    "Average profit in given year"]
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
#
# @table: list of lists
def show_table(table):
    title_list = ["ID", "Month", "Day", "Year", "Type (in/out)", "Amount ($)"]
    show_tbl = ui.print_table(table, title_list)
    return table


# Ask a new record as an input from the user than add it to @table, than return @table
#
# @table: list of lists
def add(table):

    title_list = ["Month", "Day", "Year", "Type (in/out)", "Amount ($)"]
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

# the question: Which year has the highest profit? (profit=in-out)
# return the answer (number)
def which_year_max(table):
    t_income = {}
    t_outcome = {}
    for t in table:
        if t[4] == "in":
            year = t[3]
            if year in t_income:
                t_income[year] += int(t[5])
            else:
                t_income.update({year: int(t[5])})
        elif t[4] == "out":
            year = t[3]
            if year in t_outcome:
                t_outcome[year] += int(t[5])
            else:
                t_outcome.update({year: int(t[5])})
    profit = [(t_income["2015"] - t_outcome["2015"]), (t_income["2016"] - t_outcome["2016"])]
    max_profit = max(profit)
    if max_profit == profit[0]:
        result = 2015
    elif max_profit == profit[1]:
        result = 2016
    label = "Year of highest profit is"
    result = ui.print_result(result, label)
    return result


# the question: What is the average (per item) profit in a given year? [(profit)/(items count) ]
# return the answer (number)
def avg_amount(table, year):

    # your code

    pass
