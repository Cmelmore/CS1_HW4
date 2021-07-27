"""
Author: Christina Elmore
Section Number: 02
RIN: 661542904
Assignment: HW 4 Part 1
Purpose: Determine if the user input is a palendrome.
"""

def remove_extra(word): # removes all whitespace & non-alphabetic characters, changes to lower case, and returns modified string
    word.strip()
    word.strip("0").strip("1").strip("2").strip("3").strip("4").strip("5").strip("6").strip("7").strip("8").strip("9")
    word.strip('!').strip('@').strip('#').strip('$').strip('%').strip('^').strip('&').strip('*').strip('(').strip(')')
    word.strip('-').strip('_').strip('=').strip('+').strip('[').strip('{').strip(']').strip('}')
    word.strip(';').strip(':').strip("'").strip('"').strip(',').strip('.').strip('?').strip('/')
    word.lower