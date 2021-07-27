"""
Author: Christina Elmore
Section Number: 02
RIN: 661542904
Assignment: HW 4 Part 2
Purpose: Write a program that can determine if you have enough legos to create the inputted number of the inputted type of piece.
"""
import hw4_util

def make_legos_exact(lego_type, quantity): # Tells how many legos you'll need if you don't need to combine to make more
    num_type = legos.count(lego_type) 
    if quantity <= num_type:
        result = [quantity, lego_type]
        return result
    else:
        return 'not enough'
def make_legos_sub(lego_type, quantity): # Tells how many legos you'll need if you need to make them by combining smaller pieces
    num_1x1 = legos.count('1x1')
    num_2x1 = legos.count('2x1')
    num_2x2 = legos.count('2x2')
    num_4x2 = legos.count('4x2')
    if lego_type == '1x1':
        if quantity <= (num_1x1):
            amount = (quantity)
            piece = '1x1'
        else:
            return 'not enough'        
    if lego_type == '2x1':
        if quantity <= (num_1x1 / 2):
            amount = (quantity * 2)
            piece = '1x1'
        else:
            return 'not enough'
    elif lego_type == '2x2':
        if quantity <= (num_2x1 / 2):
            amount = (quantity * 2)
            piece = '2x1'
        elif quantity <= (num_1x1 / 4):
            amount = (quantity * 4)
            piece = '1x1'
        else:
            return 'not enough'
    elif lego_type == '4x2':
        if quantity <= (num_2x2 / 2):
            amount = (quantity * 2)
            piece = '2x2'
        elif quantity <= (num_2x1 / 4):
            amount = (quantity * 4)
            piece = '2x1'
        elif quantity <= (num_1x1 / 8):
            amount = (qunatity * 8)
            piece = '1x1'
        else: 
            return 'not enough'
    result = [amount, piece]
    return result

def remove_legos(amount, lego_type): #Removes used legos from list of legos
    i = 0
    while i < amount:
        legos.remove(lego_type)
        i += 1
    return legos
    
legos = hw4_util.read_legos()
print "Current legos", legos
lego_type = raw_input('Type of lego wanted => ')
print lego_type
quantity = int(raw_input('Quantity wanted => '))
print quantity

if make_legos_exact(lego_type, quantity) == 'not enough':
    result = make_legos_sub(lego_type, quantity)
    if result == 'not enough':
        print "I don't have %d %s legos" %(quantity, lego_type)
    else:
        print "I can use %d %s legos for this" %(result[0], result[1])
        print "Remaining legos", remove_legos(result[0], result[1])
else:
    result = make_legos_exact(lego_type, quantity)
    print "I can use %d %s legos for this" %(result[0], result[1])
    print "Remaining legos", remove_legos(result[0], result[1])