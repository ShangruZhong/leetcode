"""
    56. Merge Intervals

    Use 57. Insert Interval
    @author: Shangru
    @date: 2017/01/05
"""
# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        result = []
        for interval in intervals:
            result = self.insert(result, interval)
        return result
    
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        result = []
        newleft = newInterval.start
        newright = newInterval.end
        i = 0
        while i < len(intervals):
            if intervals[i].end < newleft: 
                result.append(intervals[i])
                i += 1
                continue
            
            if newright < intervals[i].start: # finish !
                result.append(Interval(newleft, newright))
                result += intervals[i:]
                break
            
            # exisit overlap
            
            if newleft > intervals[i].start and newright < intervals[i].end:
                result += intervals[i:]
                break
            
            # newleft <= start or newright >= end
            newleft = min(newleft, intervals[i].start)
            newright = max(newright, intervals[i].end)
            
            i += 1
            
        if i == len(intervals):
            result.append(Interval(newleft, newright))
            
        return result