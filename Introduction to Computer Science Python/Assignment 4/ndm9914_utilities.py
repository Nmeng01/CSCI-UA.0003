"""
This module defines functions for user input, forms of the verb 'to be', and plural nouns.

Submitted by Nicholas Meng, NetID ndm9914
The first function returns a user input and takes parameters into account (optional)
The second function returns the verb 'to be' in correct tense (past or present) and form (third person pronouns)
The third function returns nouns as plural or singular based on inputs
"""

def ask_user_input(question, default='', min_value='', max_value=''):
    """
    This function asks the user for an integer input to some question. The function can take a default,
    minimum, and maximum value as well if the question can only have certain answers.
    """
    while True:
        str_default = f"Default: {default}. " if default else ""
        str_min_value = f"The minimum is {min_value}. " if min_value else ""
        str_max_value = f"The maximum is {max_value}. " if max_value else ""
        user_input = input(question + str_default + str_min_value + str_max_value)
        if user_input:
            user_input = int(user_input)
            if max_value and min_value:
                if max_value <= min_value:
                    return ""
            if min_value:
                min_value = int(min_value)
                if user_input < min_value:
                    continue
            if max_value:
                max_value = int(max_value)
                if user_input > max_value:
                    continue
        elif default:
            return default
        else:
            continue
        break
    return user_input


def to_be(number, tense=0):
    """
    This function determines whether to use the singular or plural form of the verb 'to be' and also
    chooses from past or present tense. The function takes integer inputs to determine these things.
    """
    if tense == 0:
        to_be_list = ["is", "are"]
        verb = to_be_list[0] if number == 1 else to_be_list[1]
    else:
        to_be_list = ["was", "were"]
        verb = to_be_list[0] if number == 1 else to_be_list[1]
    return verb


def plural(noun, number):
    """
    This function takes a noun and determines whether to return it in singular or plural form.
    """
    if number != 1:
        noun = noun + "s"
    return noun
