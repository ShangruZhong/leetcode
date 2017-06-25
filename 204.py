"""
    204. Count Primes

    Time exceed limits if use isPrime(num) and loop for each num < n
    O(n^1.5*n), so use hash_map to record the number for skipping

    @date: 2017/06/08
"""
class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        skip = [False for i in xrange(n)]
        for i in xrange(2, n):
            if not skip[i]:
                count += 1
                j = 2
                while i*j < n:
                    skip[i*j] = True
                    j += 1
        return count