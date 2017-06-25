"""
    229. Majority Element II

    Similar to 169. Majority Elements
    @date: 2017/04/27
"""

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        size = len(nums)
        if not size:
            return nums
        count = {}
        for i in xrange(size):
            if nums[i] in count:
                count[nums[i]] += 1
            elif len(count) == 2:
                self.minusOne(count)
            else:
                count[nums[i]] = 1
        res = []
        for key in count.keys():
            if self.check(nums, key):
                res.append(key)
        return res
    
    def minusOne(self, count):
        rm_list = []
        for k in count:
            count[k] -= 1
            if count[k] == 0:
                rm_list.append(k)
        for num in rm_list:
            count.pop(num)
        return count
    
    def check(self, nums, num):
        size = len(nums)
        count = 0
        for i in xrange(size):
            if nums[i] == num:
                count += 1
        return True if count > size/3 else False
        
 
        