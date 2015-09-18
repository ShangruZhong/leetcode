class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashmap = {}
        for i in range(len(nums)):
        	if target-nums[i] in hashmap:
        		return (hashmap[target-nums[i]]+1,i+1)
        	hashmap[nums[i]] = i

nums = [7,2,3,5,10,12]
obj = Solution()
print obj.twoSum(nums,9)