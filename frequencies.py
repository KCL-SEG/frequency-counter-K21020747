"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    # Your code goes here

    for x in items:
        y = str(x)
        
        if y in frequencies:
            frequencies[y] += 1
        else:
            frequencies[y] = 1

    print(frequencies)
    return frequencies
