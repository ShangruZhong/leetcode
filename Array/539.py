"""
    539. Minimum Time Difference
    
    Nice solution using bucket like bitmap, time O(n)
    Duplicate times may occur!
    
    @date: 2017/04/26
"""
class Solution(object):
    def findMinDifference(self, timePoints):
        """
        :type timePoints: List[str]
        :rtype: int
        """
        bucket = [0]*24*60
        for s in timePoints:
            time = int(s.split(':')[0])*60 + int(s.split(':')[1])
            if bucket[time]: # when duplicate time occur, min_diff must be zero
                return 0
            bucket[time] = 1
        
        first, last = -1, -1
        prev = -24*60
        min_diff = 24*60
        for i in xrange(24*60):
            if bucket[i]:
                print i, prev
                if first == -1:
                    first = i
                min_diff = min(min_diff, i - prev)
                prev = i
                last = max(last, i)
        min_diff = min(min_diff, 24*60 - last + first)
        return min_diff
            