"""
Given a string s consists of some words separated by some number of spaces, return the length of the last word in the string.

A word is a maximal substring consisting of non-space characters only.
"""

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        newstr = s.strip(" ")
        newlist = newstr.split()
        word = newlist[-1]
        return(len(word))
