"""
    268. Missing Number

    bitmap !!!
    @date: 2017/06/11
"""
class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        bitmap = len(nums)
        i = 0
        for num in nums:
            bitmap ^= num
            bitmap ^= i
            i += 1
        return bitmap 