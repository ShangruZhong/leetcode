"""
    553. Optimal Division

    @date: 2017/04/21
"""
class Solution(object):
    def optimalDivision(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        size = len(nums)
        if not size:
            return str()
        if size == 1:
            return str(nums[0])
        if size == 2:
            return str(nums[0]) + '/' + str(nums[1])
        res = str(nums[0]) + '/('
        for i in xrange(1, size - 1):
            res += str(nums[i]) + '/'
        res += str(nums[size-1]) + ')'
        return res