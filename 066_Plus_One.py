"""
Given a non-empty array of decimal digits representing a non-negative integer, increment one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array contains a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.
"""

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        def split(word):
            return[char for char in word]
        templist = list(map(str,digits))
        number = int("".join(templist))
        number = str(number + 1)
        newlist = split(number)
        newlist = list(map(int,newlist))
        return(newlist)
