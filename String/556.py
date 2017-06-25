"""
    556. Next Greater Element III

    Similar to Next Permutation
    @date: 2017/04/21
"""
class Solution(object):
    def nextGreaterElement(self, n):
        """
        :type n: int
        :rtype: int
        """
        if not n:
            return -1
        MAX_INT = (1 << 31) - 1
        n_list = [s for s in str(n)]
        self.nextPermutation(n_list)
        n_list = int("".join(n_list))
        if n_list <= n or n_list > MAX_INT:
            return -1
        else:
            return n_list

    def nextPermutation(self, nums):
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