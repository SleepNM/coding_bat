'''
Given a string, return the count of the number of times that a substring length
2 appears in the string and also as the last 2 chars of the string,
so "hixxxhi" yields 1 (we won't count the end substring).
'''

def last2(str):
    sum = 0
    for index in range(len(str)-2):
        if str[-2:] == str[index:index+2]:
            sum +=1
    return sum

# last2('hixxhi') → 1
# last2('xaxxaxaxx') → 1
# last2('axxxaaxx') → 2