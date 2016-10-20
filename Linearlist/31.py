"""
	31. Next Permutation

	Lexical Sequence, search the first one less than
	@date: 2016/10/20
"""
class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 0:
            return
        r1 = len(nums) - 2
        while r1 >= 0:
            if nums[r1] < nums[r1 + 1]:
                pivot = r1
                break
            else:
                r1 -= 1
        if r1 == -1: # list decrease, max permutation
            nums[:] = list(reversed(nums[:]))
            return
        r2 = len(nums) - 1
        while r2 > pivot:
            if nums[r2] > nums[pivot]:
                change = r2
                break
            else:
                r2 -= 1
        nums[pivot], nums[change] = nums[change], nums[pivot]
        nums[pivot + 1:] = list(reversed(nums[pivot + 1:]))
        return        