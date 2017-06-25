"""
    275. H-Index II
    
    @date: 2017/06/17
"""
class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        N = len(citations)
        l, r = 0, N - 1
        while l <= r:
            mid = l + (r - l) / 2
            if citations[mid] == N - mid:
                return N - mid
            elif citations[mid] > N - mid: # number of paper (cited>targe) < target
                r = mid - 1 # continue search left half part
            else:
                l = mid + 1
        return N - (r + 1)