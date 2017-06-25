"""
    347. Top K Frequent Elements
    
    Very important
    hashMap + quick sort
    or hashMap + minHeap
    @date: 2017/06/18
"""
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if not nums:
            return
        
        def quick_select(l, r):
            start = l
            end = r
            pivot = l
            while l < r:
                while l < r and hashMap[r][1] <= hashMap[pivot][1]:
                    r -= 1
                while l < r and hashMap[l][1] >= hashMap[pivot][1]:
                    l += 1
                hashMap[l], hashMap[r] = hashMap[r], hashMap[l]
            hashMap[pivot], hashMap[l] = hashMap[l], hashMap[pivot]
            if l + 1 == k: # index > pivot, nums[index] < nums[pivot]
                return hashMap[:l + 1]
            elif l + 1 < k:
                return quick_select(l + 1, end)
            else:
                return quick_select(start, l - 1)
                
        hashMap = {}
        for n in nums:
            hashMap[n] = hashMap.setdefault(n, 0) + 1
        hashMap = hashMap.items()
        return [kv[0] for kv in quick_select(0, len(hashMap) - 1)]