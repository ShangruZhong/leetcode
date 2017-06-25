"""
    169. Majority Element
    
    @date: 2017/04/27
"""
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        size = len(nums)
        # if not size:
        #     return 
        nums.sort()
        return nums[size/2]

    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        size = len(nums)
        # if not size:
        #     return 
        prev = nums[0]
        count = 1
        for i in xrange(1, size):
            if count == 0:
                prev = nums[i]
                count = 1
            elif nums[i] == prev:
                count += 1
            else:
                count -= 1
        return prev