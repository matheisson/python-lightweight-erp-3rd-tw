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


def send_table(table):
    data_manager.write_table_to_file(current_file_path + "/items.csv", table)


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
        which_year_max(table)
        print_which_year_max(table)
    elif option == "6":
        year = get_year()
        avg_amount(table, year)
        print_avg_amount(table, year)
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
    list_labels = ["Month", "Day", "Year", "Type (in/out)", "Amount ($)"]
    title = "Update record"
    rec_upd = ui.get_inputs(list_labels, title)
    common.update_table(table, id_, rec_upd)
    return table


# special functions:
# ------------------

# the question: Which year has the highest profit? (profit=in-out)
# return the answer (number)
def which_year_max(table):
    t_income = {}
    t_outcome = {}
    for t in table:
        if t[4] == "in":  # t[4] shows whether it is income or outcome
            year = t[3]
            if year in t_income:
                t_income[year] += int(t[5])  # adds or increases income, per year
            else:
                t_income.update({year: int(t[5])})
        elif t[4] == "out":
            year = t[3]
            if year in t_outcome:
                t_outcome[year] += int(t[5])
            else:
                t_outcome.update({year: int(t[5])})
    keys = list(t_income.keys())
    sortkeys = []
    while keys:
        minimum = keys[0]
        for x in keys:
            if x < minimum:
                minimum = x
        sortkeys.append(minimum)
        keys.remove(minimum)
    profit = []
    for key in sortkeys:
        profit.append(t_income.get(key) - t_outcome.get(key))
    max_profit = max(profit)
    for p in range(len(profit)):
        if max_profit == profit[p]:
            result = int(sortkeys[p])
    return result


def get_year():
    list_labels = ["Year:"]
    title = "What is the average (per item) profit in a given year?"
    year = ui.get_inputs(list_labels, title)
    year = int(year[0])
    return year


def print_which_year_max(table):
    result = which_year_max(table)
    label = "Highest profit in:"
    ui.print_result(result, label)


# the question: What is the average (per item) profit in a given year? [(profit)/(items count) ]
# return the answer (number)
def avg_amount(table, year):
    t_income = []
    t_outcome = []
    for t in table:
        if year == int(t[3]):
            if t[4] == "in":
                t_income.append(int(t[5]))
            elif t[4] == "out":
                t_outcome.append(int(t[5]))
    sum_t_income = 0
    for income in t_income:
        sum_t_income += income
    sum_t_outcome = 0
    for outcome in t_outcome:
        sum_t_outcome += outcome
    profit = sum_t_income - sum_t_outcome
    count_of = map(lambda x: 1, (t_income + t_outcome))
    count_of_year = len(list(count_of))
    # for y in count_of:
    #     count_of_year += y
    try:
        result = profit / count_of_year
        return result
    except ZeroDivisionError:
        msg = "Year not found."
        ui.print_error_message(msg)


def print_avg_amount(table, year):
    result = avg_amount(table, year)
    label = ""
    ui.print_result(result, label)
