"""
    303. Range Sum Query - Immutable

    @date: 2017/06/18
"""
class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        size = len(nums)
        if not size:
            self.cum = []
            return
        self.cum = [0 for i in xrange(size)]
        self.cum[0] = nums[0]
        for i in xrange(1, size):
            self.cum[i] = self.cum[i - 1] + nums[i]
        return

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        if i < 0 or i >= len(self.cum) or j < 0 or j >= len(self.cum) or i > j:
            return
        if i == 0:
            return self.cum[j]
        else:
            return self.cum[j] - self.cum[i - 1]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)