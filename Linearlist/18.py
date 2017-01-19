"""
    18. 4Sum

    Use hash map + remove duplicate items
    @date: 2016/09/15
"""
class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []
        if len(nums) < 4:
            return result
        
        inv_index = dict() 
        for a in xrange(len(nums)):
            for b in xrange(a + 1, len(nums)):
                if inv_index.has_key(nums[a] + nums[b]):
                    inv_index[nums[a]+nums[b]].append((a,b))
                else:
                    inv_index[nums[a] + nums[b]] = [(a,b)]
        
        for c in xrange(len(nums)):
            for d in xrange(c + 1, len(nums)):
                key = target - nums[c] - nums[d]
                if key not in inv_index:
                    continue
                pair_list = inv_index[key]
                for k in xrange(len(pair_list)):
                    if c <= pair_list[k][1]:
                        continue
                    result.append([nums[pair_list[k][0]], nums[pair_list[k][1]], nums[c], nums[d]])
                    
        results = []
        for each in result:
            each.sort()
        result.sort()
        for each in result:
            if each not in results:
                results.append(each)
        return results
        
                