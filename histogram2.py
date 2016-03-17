"""
File: <histogram2.py>

Copyright (c) 2016 <Paloma Leiton>

License: MIT

<brief description of the code>
"""
def digits(n):
     return len(str(n))
def histogram_2(name, tup):
    print "n | " + name
    print "---------------"
    for i in tup:
        stars = []
        for x in range(digits(i)):
            stars.append('*')
        s = ''.join(stars)
        print digits(i), " | ", s
histogram_2("Data", [4, 9, 13, 5])
#i was confused with the instructions because they ask to use the digit function, using the digits function the chart will print the length of each integer, not the amount of stars. 
