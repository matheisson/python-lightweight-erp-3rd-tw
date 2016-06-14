

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
def get_column_lenght(table, title_list):
    column_lenght = []
    column = 0
    for i in range(len(title_list)):
        column = len(title_list[i])
        for j in range(len(table)):
            if len(table[j][i]) > column:
                column = len(table[j][i])
        column_lenght.append(column)
    return column_lenght


def print_table(table, title_list):
    lenght = get_column_lenght(table, title_list)
    print()
    for i in range(len(title_list)):
        print(" " * (lenght[i] - len(title_list[i])) + title_list[i], end=" ")
    for i in range(len(table)):
        print()
        for j in range(len(title_list)):
            print(" " * (lenght[j] - len(table[i][j])) + table[i][j], end=" ")


# This function needs to print result of the special functions
#
# @result: string or list or dictionary - result of the special function
# @label: string - label of the result
def print_result(result, label):
    print(label, result)


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
    print()
    print(title)
    for i in range(len(list_options)):
        print("(%d) %s" % (((i+1) % 7), list_options[i]))
    print("(0) %s" % exit_message)

# This function gets a list of inputs from the user by the terminal
#
# @list_labels: list of strings - the labels of the inputs
# @title: string - title of the "input section"
# @inputs: list of string - list of the received values from the user


def get_inputs(list_labels, title):  # working
    inputs = []
    print(title)
    for i in range(len(list_labels)):
        user_input = input(list_labels[i] + "\t")
        inputs.append(user_input)
    return inputs


# This function needs to print an error message. (example: Error: @message)
#
# @message: string - the error message
def print_error_message(message):  # working
    print("Error: %s" % message)
