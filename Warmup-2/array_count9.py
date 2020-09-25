'''
Given an array of ints, return the number of 9's in the array.
'''


def array_count9(nums):
    sum = 0
    for num in nums:
        if num == 9:
            sum += 1
    return sum

# array_count9([1, 2, 9]) → 1
# array_count9([1, 9, 9]) → 2
# array_count9([1, 9, 9, 3, 9]) → 3
