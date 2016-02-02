"""
	84. Largest Rectangle in Histogram

	Using stack to record max value of histogram
	@author: Shangru
	@date: 2016/02/02
"""
class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        stack = []
        area = 0
        i = 0
        heights.append(0) # ensure area calculation when len(heights)=1
        while i < len(heights):
        	if len(stack) == 0 or heights[stack[-1]] < heights[i]:
        		stack.append(i)
        		i += 1
        	else:
        		top = stack[-1]
        		stack.pop()
        		if len(stack) == 0:
        			width = i
        		else: 
        			width = i-1-stack[-1]
        		area = max(area, heights[top]*width)
        return area

# s = Solution()
# s.largestRectangleArea([2,1,5,6,2,3])