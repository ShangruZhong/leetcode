"""
    165. Compare Version Numbers

    Pay attemtion to '1.0.1' vs '1'
    @date: 2017/05/11
"""
class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        version1 = version1.split('.')
        version2 = version2.split('.')
        i1 = i2 = 0
        while i1 < len(version1) and i2 < len(version2):
            a, b = int(version1[i1]), int(version2[i2])
            res = self.compare(a, b)
            if res:
                return res
            else:
                i1 += 1
                i2 += 1
        
        while i1 < len(version1):
            res = self.compare(int(version1[i1]), 0)
            if res:
                return res
            else:
                i1 += 1
            
        while i2 < len(version2):
            res = self.compare(0, int(version2[i2]))
            if res:
                return res
            else:
                i2 += 1
        return 0
        
    def compare(self, a, b):
        if a > b:
            return 1
        elif a < b:
            return -1
        else:
            return 0