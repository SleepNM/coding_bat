'''
Given two strings, return True if either of the strings appears at the very end of the other string,
ignoring upper/lower case differences (in other words, the computation should not be "case sensitive").
'''

def end_other(a, b):
    if len(a) < 3 or len(b) < 3:
        return a[-min(len(a),len(b)):].lower() == b[-min(len(a),len(b)):].lower()
    return a[-3:].lower() == b[-3:].lower()

# end_other('Hiabc', 'abc') → True
# end_other('AbC', 'HiaBc') → True
# end_other('abc', 'abXabc') → True
