"""
    16. 3Sum Closest

    @date: 2016/09/15    
"""
class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        result = 0
        if len(nums) < 3:
            return result
        nums.sort()
        min_diff = 10**10
        left = 0
        while left != len(nums) - 2:
            mid = left + 1
            right = len(nums) - 1
            
            while mid < right:
                sum = nums[left] + nums[mid] + nums[right]
                diff = abs(sum - target)
                if diff < min_diff:
                    result = sum
                    min_diff = diff
                
                if sum < target:
                    mid += 1
                else:
                    right -= 1
            left += 1
        return result