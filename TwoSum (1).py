'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
'''

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]: 
        found = False 
        returnlist = []
        y = 0
        while found == False: 
            current = nums[y]
            for x in range(len(nums)):
                if (current + nums[x] == target) and (x != y):
                    returnlist.append(y)
                    returnlist.append(x)
                    found = True
            y = y + 1
        return(returnlist)
