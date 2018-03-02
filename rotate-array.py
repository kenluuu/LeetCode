class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # for i in range(k):
        #     nums.insert(0, nums[-1])
        #     del nums[-1]
        n = len(nums)
        nums[:] = nums[n-k:] + nums[:n-k]
