"""
Given a non-negative integer x, compute and return the square root of x.

Since the return type is an integer, the decimal digits are truncated, and only the integer part of the result is returned.

Note: You are not allowed to use any built-in exponent function or operator, such as pow(x, 0.5) or x ** 0.5.
"""

#easy solution
class Solution:
    def mySqrt(self, x: int) -> int:
        return(int(x**0.5))
        
#harder solution 
class Solution:
    def mySqrt(self, x: int) -> int:
        current = 1
        while True:
            if current*current == x:
                break
            elif current*current > x:
                current -= 1
                break
            else:
                current += 1
        return(current)
