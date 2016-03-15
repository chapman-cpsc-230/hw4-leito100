"""
File: <smoothedheavyside.py>

Copyright (c) 2016 <Paloma Leiton>

License: MIT

<write a program to test the value of a number>
"""
#a
def H(x):
    if x < 0:
        value  = 0
    if x >= 0:
        value = 1
    return value

#b
def test_H():
    if H(-10) != 0:
        print "Error"
    elif H(-10 ** -15) != 0:
        print "Error"
    elif H(10 ** 15) != 1:
        print "Error"
    elif H(10) != 1:
        print "Error"
    else:
        print "Everything is correct"



test_H()
