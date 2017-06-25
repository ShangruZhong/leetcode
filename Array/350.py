"""
    350. Intersection of Two Arrays II

    @date: 2017/06/19
"""
class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        hashMap1 = {}
        hashMap2 = {}
        for n in nums1:
            hashMap1[n] = hashMap1.setdefault(n, 0) + 1
        for n in nums2:
            hashMap2[n] = hashMap2.setdefault(n, 0) + 1
        res = []
        for n in hashMap1:
            if n in hashMap2:
                for i in xrange(min(hashMap1[n], hashMap2[n])):
                    res.append(n)
        return res
            
                