"""
    128. Longest Consecutive Sequence
    
    Notice num can be duplicate
    Union Find, similar to Friend Circles
    @date: 2017/05/03
"""
class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = set(nums)
        if len(nums) == 1:
            return 1
        longest = 0
        for a in nums:
            if a - 1 not in nums: 
                next = a + 1
                while next in nums:
                    next += 1
                longest = max(longest, next - a)
        return longest