"""
    49. Group Anagrams

    @date: 2016/10/20
"""
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        hashMap = dict()
        for s in strs:
            key = ''.join(sorted(s)) 
            if key in hashMap:
                hashMap[key].append(s)
            else:
                hashMap[key] = [s]
        res = []
        for k in hashMap:
            value = hashMap[k]
            value.sort()
            res.append(value)
        return res