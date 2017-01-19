"""
	136. Single Number

	Exclusive OR
	@date: 2016/09/14
"""
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = nums[0]
        for i in xrange(1, len(nums)):
            a ^= nums[i]
        return a