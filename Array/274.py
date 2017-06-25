"""
    274. H-Index

    @date: 2017/06/17
"""
class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        N = len(citations)
        count = [0 for i in xrange(N + 1)]
        # if not N:
        #     return 0
        for c in citations:
            if c > N:
                count[N] += 1
            else:
                count[c] += 1
        total = 0
        i = N
        while i >= 0:
            total += count[i]
            if total >= i:
                return i
            i -= 1
        return 0