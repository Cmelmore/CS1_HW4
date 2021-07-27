"""
Author: Christina Elmore
Section Number: 02
RIN: 661542904
Assignment: HW 4 Part 1
Purpose: Determine if the user input is a palendrome.
"""

def remove_extra(string): # removes all whitespace & non-alphabetic characters, changes to lower case, and returns modified string
    word = list(string.lower())
    word2 = list(string.lower())    
    j = []
    i = 0
    while i < len(string):
        if word[i].isalpha() == False:
            j.append(i)
            i += 1
        else:
            i += 1
    i = 0
    while i < len(word):
        if i in j:
            word2.remove(word[i])
            i += 1
        else:
            i += 1
    return word2

def failed_pal(word, reversed_word):
    i = 0
    j = []
    while i < len(word):
        if word[i] == reversed_word[i]:
            i += 1
        else:
            j.append(i)
            i += 1
    return j[1]-1

word = raw_input('Enter a word or a sentence => ')
print word
list_word = remove_extra(word)
rev_list = list_word[::-1]
rev_word = ''.join(rev_list)
stripped_word = ''.join(list_word)

print''
print 'String after removing non-alphabetic characters:', stripped_word
print 'String reversed:', rev_word

if stripped_word == rev_word:
    print "Palindrome"
else:
    j = failed_pal(stripped_word, rev_word)
    if stripped_word[j] < rev_word[j]:
        print "Not a palindrome: %s comes before %s at position %d" %(stripped_word[j], rev_word[j], j)
    else:
        print "Not a palindrome: %s comes after %s at position %d" %(stripped_word[j], rev_word[j], j)