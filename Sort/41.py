"""
	41. First Missing Positive

	Bucket Sort
	@date: 2016/05/27
"""
class Solution(object):
	def firstMissingPositive(self, nums):
		"""
        :type nums: List[int]
        :rtype: int
        """
		self.bucketSort(nums)
		for i in xrange(len(nums)):
			if nums[i] != (i + 1):
				return i + 1
		return len(nums) + 1

	def bucketSort(self, nums):
		for i in xrange(len(nums)):
			while nums[i] != i + 1:
				if nums[i] <= 0 or nums[i] > len(nums) or nums[i] == nums[nums[i]-1]:
					break
				nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
				# Notice: nums[i] change will influence nums[nums[i]-1]

