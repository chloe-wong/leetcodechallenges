"""
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.
"""

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        returnval = -1
        x = 0
        checked = 0
        current = nums[x]
        while True:
            if current >= target:
                returnval = x
                break

            else:
                x = x + 1
                try:
                    current = nums[x]
                except IndexError: 
                    returnval = len(nums)
                    break
        return(returnval)
