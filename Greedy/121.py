"""
    121. Best Time to Buy and Sell Stock

    @date: 2016/01/05  
"""
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        days = len(prices)
        max_profit = 0
        min_price = 2**32 - 1
        for i in xrange(days):
            min_price = min(prices[i], min_price)
            max_profit = max(max_profit, prices[i] - min_price)
        return max_profit