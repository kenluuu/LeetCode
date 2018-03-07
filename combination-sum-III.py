class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """

        res = []

        def combinationSum3Util(i, sum, nums):
            if len(nums) > k: return
            if sum == n and len(nums) == k:
                res.append(nums)
                return True
            while i <= n-k:
                if sum + i + 1 > n or i+1 > 9:
                    return
                combinationSum3Util(i+1, sum+i+1, nums + [i+1])
                i += 1

        for i in range(1, n-k):
            combinationSum3Util(i, i, [i])


        return res
