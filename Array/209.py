"""
    209. Minimum Size Subarray Sum

    solution 1: sliding window !!!
    solution 2: awesome with binary search !!!
    @date: 2017/06/10
"""
class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        size = len(nums)
        i = j = 0
        sm = 0
        minLen = (1<<31) + 1
        flag = 0
        while i < size:
            sm += nums[i]
            i += 1
            while sm >= s:
                flag = 1
                minLen = min(i - j, minLen)
                sm -= nums[j]
                j += 1
        return minLen if flag else 0