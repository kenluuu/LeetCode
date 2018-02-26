class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
      
        memo = {}
        def findAll(i):
            if i in memo: return memo[i]
            if i == 0: return 1 
            elif i < 0: return 0
            result = 0
            result = findAll(i-1) + findAll(i-2)
            memo[i] = result
            return result
        return findAll(n)
