"""
Author: Christina Elmore
Section Number: 02
RIN: 661542904
Assignment: HW 4 Part 3
Purpose: Write a program to read the death statistics for different areas of NYS from 2003 to 2013 and indicate when the statistic deviates from the average.
"""
import hw4_util
import sys

def county_deaths(county): #returns a list indicating if each value for the county is more or less than 5% away from the average for that county
    cdata = hw4_util.read_deaths(county)
    average = sum(cdata)/11
    deviation = []
    i = 0
    while i < len(cdata):
        if cdata[i] >= (average + average * .05):
            deviation.append('+')
            i += 1
        elif cdata[i] <= (average - average * .05):
            deviation.append('-')
            i += 1
        else:
            deviation.append('=')
            i += 1
    return deviation

county1 = raw_input('First county => ')
print county1
county2 = raw_input('Second county => ')
print county2
print ''

i = 0
if county_deaths(county1) == []:
    print "I could not find county", county1
    i += 1
if county_deaths(county2) == []:
    print "I could not find county", county2
    i += 1
if i > 0:
    sys.exit()

print " " * 14 , 2013, " ", 2003
print county1, " " * (13 - len(county1)), "".join(county_deaths(county1))
print county2, " " * (13 - len(county2)), "".join(county_deaths(county2))