'''
Return the number of even ints in the given array.
'''


def count_evens(nums):
    even = 0
    for num in nums:
        if num % 2 == 0:
            even += 1
    return even

# count_evens([2, 1, 2, 3, 4]) → 3
# count_evens([2, 2, 0]) → 3
# count_evens([1, 3, 5]) → 0
