"""
    295. Find Median from Data Stream

    Problem from Jianzhi Offer 
    @date: 2017/06/13
"""
class MedianFinder(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        import heapq
        self.minHeap = []
        self.maxHeap = []

    def addNum(self, num):
        """
        :type num: int
        :rtype: void
        """
        if (len(self.minHeap) + len(self.maxHeap)) & 1: # odd number
            if len(self.minHeap) > 0 and num > self.minHeap[0]:
                heapq.heappush(self.minHeap, num)
                num = heapq.heappop(self.minHeap)
            heapq.heappush(self.maxHeap, -num)
        else:
            if len(self.maxHeap) > 0 and num < -self.maxHeap[0]:
                heapq.heappush(self.maxHeap, -num)
                num = -heapq.heappop(self.maxHeap)
            heapq.heappush(self.minHeap, num)

    def findMedian(self):
        """
        :rtype: float
        """
        size = len(self.maxHeap) + len(self.minHeap)
        if size:
            if size & 1:
                return self.minHeap[0]*1.0
            else:
                return (-self.maxHeap[0] + self.minHeap[0])/2.0
        else:
            return None


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()