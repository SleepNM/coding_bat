'''
Given a string, return a string where for every char in the original, there are two chars.
'''

def double_char(str):
    new_word = ''
    for i in str:
        new_word += i * 2
    return new_word

# double_char('The') → 'TThhee'
# double_char('AAbb') → 'AAAAbbbb'
# double_char('Hi-There') → 'HHii--TThheerree'
