"""
Given two binary strings a and b, return their sum as a binary string.
"""

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        num1,num2 = int(a,base=2),int(b,base=2)
        return(str(bin(num1+num2))[2:])
