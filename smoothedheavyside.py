"""
File: <smoothedheavyside.py>

Copyright (c) 2016 <Paloma Leiton>

License: MIT

<testing different values>
"""


import math
def H_eps(x, eps = 0.01):
    answer = 0
    if x < (-1 * eps):
        answer = 0
    elif (x >= (-1 * eps) and (x <= eps)):
        answer = .5 + (x/(2 * eps)) + ((1/2 * math.pi) * math.sin(math.pi * x )/ eps)
    else:
        answer = 1
    return answer

def test_H_eps():
    print "-1", H_eps(-1)
    print "-0.01", H_eps(-0.01)
    print "0", H_eps(0)
    print "0.01", H_eps(0.01)
    print "1", H_eps(1)

test_H_eps()
