"""
    220. Contains Duplicate III

    Submit 7 times and accept 1...
    find nums meet diff < maxDiff in a sorted array
    @date: 2017/06/10 
"""
class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        if not nums:
            return False
        numsSort = sorted(nums)
        for i in xrange(len(numsSort)):
            j = i + 1
            while j < len(numsSort) and numsSort[j] - numsSort[i] <= t:
                prev, cur = numsSort[i], numsSort[j]
                if cur != prev:
                    index1 = index2 = None
                    for ii in xrange(len(nums)):
                        if nums[ii] == prev:
                            index1 = ii
                        elif nums[ii] == cur:
                            index2 = ii
                    if abs(index1 - index2) <= k:
                        return True
                else:
                    index1 = nums.index(prev)
                    for ii in xrange(index1 + 1, len(nums)):
                        if nums[ii] == prev:
                            if abs(ii - index1) <= k:
                                return True
                            else:
                                index1 = ii
                j += 1
        return False