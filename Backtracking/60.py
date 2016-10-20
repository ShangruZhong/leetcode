"""
	60. Permutation Sequence

	Solution:
		- Naive: calling nextPermutation() for k-1 times
		- Effective: consider sub-permutation
	date: 2016/10/20
"""
import math
class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        nums =str()
        for i in xrange(1, n + 1):
            nums += str(i)
        return self.kthPermutation(nums, n, k)
    
    def factorial(self, n):
        if n == 0:
            return 1
        else:
            return n*self.factorial(n - 1)

    def kthPermutation(self, nums, n, k):
        res = str()
        i = 1
        while i <= n :
            tmp = self.factorial(n - i)    
            index = int(math.ceil(k / float(tmp))) - 1
            char = nums[index]
            res += char

            k = k % tmp
            nums = list(nums)
            nums.remove(char)
            nums = ''.join(nums)
            i += 1
        return res