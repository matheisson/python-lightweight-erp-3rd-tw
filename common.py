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


def add_to_table(table, title_list):
    inputs = ui.get_inputs(title_list, "Please enter:")
    inputs.insert(0, generate_random(table))
    table.append(inputs)
    return table


def get_id():
    list_labels = ["ID"]
    title = "Update/Remove record with the following ID"
    id_ = ui.get_inputs(list_labels, title)
    return id_


def remove_table(table, id_):
    for t in table:
        if t[0] == id_[0]:
            table.remove(t)
    return table


def update_table(table, id_, updated_data):
    for t in table:
        if t[0] == id_[0]:
            for x in range(len(updated_data)):
                t[x+1] = updated_data[x]
    return table
