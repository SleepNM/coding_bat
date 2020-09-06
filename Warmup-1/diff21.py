'''
Given an int n, return the absolute difference between n and 21,
except return double the absolute difference if n is over 21.
'''

def diff21(n):
    sum = abs(n-21)
    if n > 21:
        return sum*2
return sum


# diff21(19) → 2
# diff21(10) → 11
# diff21(21) → 0