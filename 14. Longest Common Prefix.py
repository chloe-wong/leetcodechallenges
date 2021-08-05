"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".
"""

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pref = ""
        flag = True
        x = 0
        while flag == True:
            print(pref)
            try:
                pref = pref + strs[0][x]
            except IndexError:
                return(pref)

            for y in range(len(strs)):
                if strs[y][0:x+1] != pref:
                    flag = False
            x = x + 1
        pref = pref[:-1]
        return(pref)
