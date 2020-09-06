'''
Given a string of even length, return the first half. So the string "WooHoo" yields "Woo".
'''

def first_half(str):
    return str[:(len(str)+1)/2]

# first_half('WooHoo') → 'Woo'
# first_half('HelloThere') → 'Hello'
# first_half('abcdef') → 'abc'
