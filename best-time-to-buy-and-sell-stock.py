class Solution(object):
    def maxProfit(self, prices):
        if len(prices) == 0: return 0
        currMin = prices[0]
        currMax = 0
        for i in range(0, len(prices)):
            if prices[i] < currMin:
                currMin = prices[i]
            else:
                if prices[i] - currMin > currMax:
                    currMax = prices[i] - currMin

        return currMax
