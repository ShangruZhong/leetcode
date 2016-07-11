"""
	11. Container With Most Water

	@date: 2016/07/11
"""
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        left = 0
        right = n-1
        tmp = 0 
        while left < right:
            area = min(height[left], height[right])*(right - left)
            if tmp < area:
                tmp = area
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
        return tmp
