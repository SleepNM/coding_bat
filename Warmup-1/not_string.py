'''
Given a string, return a new string where "not " has been added to the front.
However, if the string already begins with "not", return the string unchanged.
'''


def not_string(str):
    new = "not "
    if str[0:3] == new[0:3]:
        return str
    else:
        return new + str


# not_string('candy') → 'not candy'
# not_string('x') → 'not x'
# not_string('not bad') → 'not bad'
