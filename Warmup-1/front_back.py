'''
Given a string, return a new string where the first and last chars have been exchanged.
'''

def front_back(str):
    if len(str) <= 1:
        return str
    else:
        new = [x for x in str]
        new1 = new[0]
        new2 = new[-1]
        new[0] = new2
        new[-1] = new1
        return ''.join(new)


# front_back('code') → 'eodc'
# front_back('a') → 'a'
# front_back('ab') → 'ba'