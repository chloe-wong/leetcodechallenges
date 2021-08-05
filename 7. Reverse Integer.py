"""
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).
"""

class Solution:
    def reverse(self, x: int) -> int:
        if str(x)[0] =='-':
            flipstring = str(x)[1:]
            newnum = int('-' + flipstring[::-1])
        else:
            newnum = int(str(x)[::-1])
        if (newnum > (2**31 - 1)) or (newnum < (-2)**31):
            return 0
        else:
            return newnum
