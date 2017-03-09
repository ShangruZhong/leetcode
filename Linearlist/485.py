"""
    485. Max Consecutive Ones

    @date: 2017/03/09
"""
class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not len(nums):
            return 0
        if nums[0] == 1:
            count = 1
        else:
            count = 0
        maxcount = count
        for i in xrange(1, len(nums)):
            if nums[i] == 1:
                if nums[i] == nums[i-1]:
                    count += 1
                else:
                    count = 1
            else:
                count = 0
            maxcount = max(maxcount, count)
        return maxcount