#!/usr/bin/env python
# implement commonly used functions here


import random
import ui
import string


# generate and return a unique and random string
# other expectation:
# - at least 2 special char()expect: ';'), 2 number, 2 lower and 2 upper case letter
# - it must be unique in the list
#
# @table: list of list
# @generated: string - generated random string (unique in the @table)
def generate_random(table):  # working
    good_pw = [0, 0, 0, 0]
    chars = string.ascii_letters + string.digits + "[!@#$%^&*()?]"
    generated = []
    for i in range(8):
        generated.append(random.choice(chars))
    for i in range(8):
        if generated[i] in string.ascii_lowercase:
            good_pw[0] += 1
        elif generated[i] in string.ascii_uppercase:
            good_pw[1] += 1
        elif generated[i] in string.digits:
            good_pw[2] += 1
        elif generated[i] in "[!@#$%^&*()?]":
            good_pw[3] += 1
    generated = "".join(generated)
    if good_pw == [2, 2, 2, 2]:
        for i in range(len(table)):
            if generated not in str(table[i][0]):
                return generated
            else:
                return generate_random(table)
    else:
        return generate_random(table)

'''
def generate_start(title, function_list, go_back):
    print(title)
    for i in range(len(function_list)):
        print("(%d) %s" % (((i+1) % 7), function_list[i]))
    print("(0) %s" % go_back)'''


def forward_table(title):
    if title == "Accounting Manager":
        return data_manager.get_table_from_file("items.csv")
    elif title == "crm":
        return data_manager.get_table_from_file("costumers.csv")
    elif title == "hr":
        return data_manager.get_table_from_file("persons.csv")
    elif title == "selling":
        return data_manager.get_table_from_file("sellings.csv")
    elif title == "store":
        return data_manager.get_table_from_file("games.csv")
    elif title == "tool man":
        return data_manager.get_table_from_file("tools.csv")
