"""
    74. Search a 2D Matrix

    @date: 2017/02/17
"""
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        nums = []
        for i in xrange(len(matrix)):
            nums += matrix[i]
        nums.sort()
        return self.binarySearch(nums, target)
    
    def binarySearch(self, nums, target):
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r)/2
            if nums[mid] == target:
                return True
            elif nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        return False