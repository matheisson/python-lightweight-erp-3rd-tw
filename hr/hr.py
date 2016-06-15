# data structure:
# id: string
#     Unique and random generated (at least 2 special char()expect: ';'), 2 number, 2 lower and 2 upper case letter)
# name: string
# birth_date: number (year)


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
#
file_name = "hr/persons.csv"


def get_table():
    return data_manager.get_table_from_file(current_file_path + "/persons.csv")


def choose_function(table):
    table = get_table()
    inputs = ui.get_inputs(["Please enter a number: "], "")
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
        get_oldest_person(table)
        print_oldest_person(table)
    elif option == "6":
        get_persons_closest_to_average(table)
        print_get_persons(table)
    elif option == "0":
        return "break"
    else:
        raise KeyError("There is no such option.")


def start_module():
    title = "HR"
    functions = ["Show Table", "Add to Table", "Remove from Table", "Update Element", "Oldest Person",
                 "Closest to Average"]
    back = "Back to Main Menu"
    table = get_table()
    while True:
        ui.print_menu(title, functions, back)
        try:
            valid = choose_function(table)
            if valid == "break":
                break
        except KeyError as err:
            ui.print_error_message(err)


def show_table(table):
    title_list = ["ID\t", "Name\t", "Age\t"]
    solution = data_manager.get_table_from_file(file_name)
    ui.print_table(table, title_list)


# Ask a new record as an input from the user than add it to @table, than return @table
#
# @table: list of lists
def add(table):
    title_list = ["Name", "Birth_Year"]
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
    list_labels = ["Name", "Birth year"]
    title = "Update record"
    rec_upd = ui.get_inputs(list_labels, title)
    common.update_table(table, id_, rec_upd)
    return table


# special functions:
# ------------------

# the question: Who is the oldest person ?
# return type: list of strings (name or names if there are two more with the same value)
def get_oldest_person(table):
    sol = []
    names = []
    result = []
    for line in table:
        years = line[2]
        name = line[1]
        names.append(name)
        sol.append(int(years))
    min_ = sol[0]
    for i in range(len(sol)):
        if sol[i] < min_:
            min_ = sol[i]
            result = []
            result.append(names[i])
        elif sol[i] == min_:
            result.append(names[i])
    return result


def print_oldest_person(table):
    result = get_oldest_person(table)
    label = ""
    ui.print_result(result, label)


# the question: Who is the closest to the average age ?
# return type: list of strings (name or names if there are two more with the same value)
def get_persons_closest_to_average(table):
    years = []
    names = []
    avg = 0
    # calc average
    for line in table:
        name = line[1]
        names.append(name)
        year = line[2]
        years.append(int(year))
    for i in years:
        avg += i
    avg = int(avg / len(table))
    # calc closest
    closest = years[0]
    for i in range(len(years)):
        if abs(years[i] - avg) < closest:
            closest = abs(years[i] - avg)
            result = []
            result.append(names[i])
        elif abs(years[i] - avg) == closest:
            result.append(names[i])
    return result


def print_get_persons(table):
    result = get_persons_closest_to_average(table)
    label = ""
    ui.print_result(result, label)
