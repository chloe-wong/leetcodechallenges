"""
Given a string s, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleanstring = ""
        for x in s:
            if 65 <= ord(x) <= 90 or 97 <= ord(x) <= 122 or 48 <= ord(x) <= 57:
                cleanstring = cleanstring + x.lower()
        if cleanstring == cleanstring[::-1]:
            return True
        else:
            return False
