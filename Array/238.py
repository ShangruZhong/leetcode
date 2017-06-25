"""
    238. Product of Array Except Self

    No division but require O(n) extra space
    @date: 2017/06/17
"""
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        size = len(nums)
        if not size:
            return 
        prodFromBegin = [1 for i in xrange(size)]
        prodFromEnd = [1 for i in xrange(size)]
        res = [0 for i in xrange(size)]
        for i in xrange(1, size):
            prodFromBegin[i] = prodFromBegin[i - 1] * nums[i - 1]
            prodFromEnd[i] = prodFromEnd[i - 1] * nums[size - i]
        for i in xrange(size):
            res[i] = prodFromBegin[i] * prodFromEnd[size - 1 - i]
        return res