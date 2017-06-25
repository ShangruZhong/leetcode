"""
    217. Contains Duplicate

    Very Easy
    @date: 2017/06/10
"""
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not len(nums):
            return False
        hashMap = {}
        for num in nums:
            if num in hashMap:
                return True
            else:
                hashMap[num] = 1
        return False