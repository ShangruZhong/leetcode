"""
	55. Jump Game

	@date: 2016/05/31
"""
class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        maxTop = 1
        i = 0
        while i < maxTop and maxTop < len(nums):
            maxTop = max(maxTop, i + 1 + nums[i])
            i += 1
        return maxTop >= len(nums)