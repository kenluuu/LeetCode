class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        dict = {}
        candidates.sort()
        def findComb(stack, remain, index, key):
            if remain == 0:
                if key not in dict:
                    res.append(stack)
                    dict[key] = 1
                return
            for i in range(index, len(candidates)):
                if candidates[i] > remain: break
                findComb(stack + [candidates[i]], remain-candidates[i], i+1, key + str(candidates[i]))
