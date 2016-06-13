

# This function needs to print outputs like this:
# /-----------------------------------\
# |   id   |      title     |  type   |
# |--------|----------------|---------|
# |   0    | Counter strike |    fps  |
# |--------|----------------|---------|
# |   1    |       fo       |    fps  |
# \-----------------------------------/
#
# @table: list of lists - the table to print out
# @title_list: list of strings - the head of the table
def print_table(table, title_list):

    # your code

    pass


# This function needs to print result of the special functions
#
# @result: string or list or dictionary - result of the special function
# @label: string - label of the result
def print_result(result, label):
    print(label)
    print(result)


# This function needs to generate outputs like this:
# Main menu:
# (1) Store manager
# (2) Human resources manager
# (3) Inventory manager
# (4) Accounting manager
# (5) Selling manager
# (6) Customer relationship management (CRM)
# (0) Exit program
#
# @title: string - title of the menu
# @list_options: list of strings - the options in the menu
# @exit_message: string - the last option with (0) (example: "Back to main menu")
def print_menu(title, list_options, exit_message):  # working
    print(title)
    for i in range(len(list_options)):
        print("(%d) %s" % (((i+1) % 7), list_options[i]))
    print(exit_message)

# This function gets a list of inputs from the user by the terminal
#
# @list_labels: list of strings - the labels of the inputs
# @title: string - title of the "input section"
# @inputs: list of string - list of the received values from the user


def get_inputs(list_labels, title):  # working
    inputs = []
    print(title)
    for i in range(len(list_labels)):
        user_input = input(list_labels[i] + ": ")
        inputs.append(user_input)

    return inputs


# This function needs to print an error message. (example: Error: @message)
#
# @message: string - the error message
def print_error_message(message):

    # your code

    pass

'''title = "hello"
list_options = ["elso", "masodik", "harmadik", "negyedik", "otodik", "hatodik"]
exit_message = "bye"

print_menu(title, list_options, exit_message)
'''
'''label = "csao"
result = ["hali", 3, "csecs", ["alma", 2]]
print_result(result, label)'''
'''list_labels = ["1", "masodik"]
title = "Input section"
get_inputs(list_labels, title)'''
