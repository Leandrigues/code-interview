class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profit = 0
        candidate_buy = 0

        for i, price in enumerate(prices):
            candidate_buy = i if price < prices[candidate_buy] else candidate_buy
            if candidate_buy < i and prices[i] - prices[candidate_buy] > max_profit:
                max_profit = prices[i] - prices[candidate_buy]

        return max_profit

print(Solution().maxProfit([7,6,4,3,1]))
