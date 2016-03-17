"""
File: <histogram.py>

Copyright (c) 2016 <Paloma Leiton>

License: MIT

<prints a certain number of stars for each digit>
"""
ls = [4, 9, 13, 5]
def bar(n):
    st = ''
    for i in range(n):
        st += '*'
    return st

for i in range(len(ls)):
    print bar(ls[i])
print ls
