# data structure:
# id: string
#     Unique and random generated (at least 2 special char()expect: ';'), 2 number, 2 lower and 2 upper case letter)
# title: string
# price: number (the actual selling price in $)
# month: number
# day: number
# year: number
# month,year and day combined gives the date the purchase was made


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
    return data_manager.get_table_from_file(current_file_path + "/sellings.csv")


def send_table(table):
    data_manager.write_table_to_file(current_file_path + "/sellings.csv", table)


def print_sold_between(table, month_from, day_from, year_from, month_to, day_to, year_to):
    result = get_items_sold_between(table, month_from, day_from, year_from, month_to, day_to, year_to)
    label = "Titles sold during these dates:"
    ui.print_result(result, label)


def print_lowest_price_item(table):
    result = get_lowest_price_item_id(table)
    label = "ID of lowest priced item:"
    ui.print_result(result, label)


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
        get_lowest_price_item_id(table)
        print_lowest_price_item(table)
    elif option == "6":
        dates = get_dates()
        month_from = dates[0]
        month_from = dates[0]
        day_from = dates[1]
        year_from = (dates[2])
        month_to = dates[3]
        day_to = dates[4]
        year_to = dates[5]
        get_items_sold_between(table, month_from, day_from, year_from, month_to, day_to, year_to)
        print_sold_between(table, month_from, day_from, year_from, month_to, day_to, year_to)
    elif option == "0":
        return "break"
    else:
        raise KeyError("There is no such option.")


# start this module by a module menu like the main menu
# user need to go back to the main menu from here
# we need to reach the default and the special functions of this module from the module menu
#
def start_module():
    title = "Selling Manager"
    list_options = ["Show Table", "Add to Table", "Remove from Table", "Update Element", "Lowest Price",
                    "Items sold between"]
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
    title_list = ["ID", "Title", "Price", "Month", "Day", "Year"]
    show_tbl = ui.print_table(table, title_list)
    return table


# Ask a new record as an input from the user than add it to @table, than return @table
#
# @table: list of lists
def add(table):
    title_list = ["Title", "Price", "Month", "Day", "Year"]
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
    list_labels = ["Title", "Price", "Month", "Day", "Year"]
    title = "Update record"
    rec_upd = ui.get_inputs(list_labels, title)
    common.update_table(table, id_, rec_upd)
    return table


# special functions:
# ------------------

# the question: What is the id of the item that sold for the lowest price ?
# return type: string (id)
# if there are more than one with the lowest price, return the first of descending alphabetical order
def get_lowest_price_item_id(table):
    prices = []
    for t in table:
        prices.append(t[2])
    sortprices = []
    while prices:
        minimum = prices[0]
        for x in prices:
            if x < minimum:
                minimum = x
        sortprices.append(minimum)
        prices.remove(minimum)
    lowest = min(sortprices)
    for t in table:
        if t[2] == lowest:
            result = t[0]
    return result


def get_dates():
    list_labels = ["month from", "day from", "year from", "month to", "day to", "year to"]
    title = "Which items are sold between two given dates?"
    dates = ui.get_inputs(list_labels, title)
    return dates


# the question: Which items are sold between two given dates ? (from_date < birth_date < to_date)
# return type: list of lists (the filtered table)
def get_items_sold_between(table, month_from, day_from, year_from, month_to, day_to, year_to):
    items = []
    for t in table:
        if int(t[5]) > int(str(year_from)) and int(t[5]) < int(str(year_to)):
            items.append(t)
        if (int(t[5]) == int(str(year_from))) or (int(t[5]) == int(str(year_to))):
            if int(t[3]) > int(month_from) and int(t[3]) < int(month_to):
                items.append(t)
            if (int(t[3]) == int(str(month_from))) or (int(t[3]) == int(str(month_to))):
                if int(t[4]) > int(day_from) and int(t[4]) < int(day_to):
                    items.append(t)
    result = []
    for t in range(len(items)):
        items[t][2] = int(items[t][2])
        items[t][3] = int(items[t][3])
        items[t][4] = int(items[t][4])
        items[t][5] = int(items[t][5])
    return items
