"""
    287. Find the Duplicate Number  

    classical binary search application !
    @date: 2017/06/13
"""
class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l, r = 1, len(nums) - 1
        while l < r:
            mid = l + (r  - l) / 2
            count = 0
            for num in nums:
                if num <= mid:
                    count += 1
            if count <= mid:
                l = mid + 1
            else:
                r = mid
        return l