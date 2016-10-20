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
            r1 -= 1
        if r1 == -1: # list decreases, max permutation
            nums[:] = list(reversed(nums[:])) # reversed the whole list
            return
        r2 = len(nums) - 1
        while r2 > pivot:
            if nums[r2] > nums[pivot]: # from right to left, the first one larger than nums[pivot]
                change = r2  # nums[change] > nums[pivot]
                break
            else:
                r2 -= 1
        nums[pivot], nums[change] = nums[change], nums[pivot] # after swap, the list[pivot+1:] decreases
        nums[pivot + 1:] = list(reversed(nums[pivot + 1:])) # reversed the list[pivot:]
        return
        