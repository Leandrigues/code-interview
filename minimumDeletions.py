from calendar import c
from re import A
from tkinter import E


class Solution(object):
    def minDeletions(self, s):
        """
        :type s: str
        :rtype: int
        """
        num_array = [0] * (len(s) + 1)
        char_dict = {}
        deletes = 0
        for char in s:
            if char in char_dict:
                char_dict[char] += 1
            else:
                char_dict[char] = 1
        print(char_dict)

        for char in char_dict:
            num_array[char_dict[char]] += 1
        print(num_array)

        for i, num in enumerate(reversed(num_array)):
            if num > 1 and i < len(num_array):
                index = len(num_array) - i - 1
                num_array[index - 1] += num_array[index] - 1
                print(num_array)
                deletes += num_array[index] - 1
                print(index)
        print(deletes)
        return deletes

Solution().minDeletions("aaabbbc")
# bbbb
# c
# e
# a
