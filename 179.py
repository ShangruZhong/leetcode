"""
    179. Largest Number

    Define sort rule: a ">" b only when ab > ba
    sort string and convert to integer
    @date: 2017/02/24
"""
class Solution:
    # @param {integer[]} nums
    # @return {string}
    def largestNumber(self, nums):
        if not nums:
            return "0"
        lmb = lambda n1, n2:int(str(n1)+str(n2))-int(str(n2)+str(n1))
        res = sorted(nums, cmp=lmb, reverse=True)
        if res[0] == 0: # res = [0, 0, 0] => "0"
            return "0"
        return "".join([str(n) for n in res])

    # solution 2
    def largestNumber(self, nums):
        if not nums:
            return "0"
        from operator import add
        strs = map(str, nums)
        lmb = lambda x, y:cmp(int(y+x), int(x+y))
        return str(int(reduce(add, sorted(strs, cmp=lmb))))