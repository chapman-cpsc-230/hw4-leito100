"""
File: <count_pairs.py>

Copyright (c) 2016 <Paloma Leiton>

License: MIT

<program that returns the number of occurences of a pair of characters.>
"""
def countpairs(dna, pair):
    pairs = 0
    i = 0
    while (i < len(dna)):
        index = dna.find(pair, i)
        if (index != -1):
            pairs += 1
            i = index
        i += 1
    print "There are ", pairs, "pairs!"

countpairs( "AGTAGGGATA", "AG")
