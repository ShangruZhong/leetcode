"""
    384. Shuffle an Array

    Important ! how to generate permutations randomly
    @date: 2017/06/19    
"""
class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        return self.nums

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        import random
        tmp = self.nums[:]
        size = len(tmp)
        for i in xrange(size):
            pos = random.randint(0, 65536) % (size - i)
            tmp[i], tmp[i + pos] = tmp[i + pos], tmp[i]
        return tmp


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()