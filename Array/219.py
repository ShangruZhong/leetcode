"""
    219. Contains Duplicate II

    Also very easy like 217
    @date: 2017/06/10
"""
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        size = len(nums)
        if not size:
            return False
        hashMap = {}
        for i in xrange(size):
            if nums[i] in hashMap:
                if i - hashMap[nums[i]] <= k:
                    return True
                else:
                    hashMap[nums[i]] = i
            else:
                hashMap[nums[i]] = i
        return False