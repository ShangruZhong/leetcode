"""
    349. Intersection of Two Arrays

    @date: 2017/06/18
"""
class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        hashMap = {}
        for n in set(nums1):
            hashMap[n] = hashMap.setdefault(n, 1)
        res = []
        for n in set(nums2):
            if n in hashMap:
                res.append(n)
        return res