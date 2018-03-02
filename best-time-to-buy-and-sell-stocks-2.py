class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) < 2: return 0
        profit = 0
        curr = prices[0]
        curr_max = 0
        for i in range(1, len(prices)):
            if prices[i] > curr and prices[i] > curr_max:
                curr_max = prices[i]
                continue
            if curr_max == 0:
                curr = prices[i]
            else:
                profit += (curr_max - curr)
                curr = prices[i]
                curr_max = 0
        if curr_max > 0: profit += (curr_max - curr)


        return profit
