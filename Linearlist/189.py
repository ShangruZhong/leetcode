"""
    189. Rotate Array

    rotate array, similar to rotate string
    @date: 2017/02/24
"""
class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if k < 0 or not len(nums):
            return
        length = len(nums)
        k = k%length
        self.reverse(nums, 0, length - 1 - k)
        self.reverse(nums, length - k, length - 1)
        self.reverse(nums, 0, length - 1)

    def reverse(self, nums, l, r):
        while l <= r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
        return nums