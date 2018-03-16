class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        l = 0
        r = len(nums)-1
        i = None

        while l <= r:
            mid = (r+l)/2
            if nums[mid] == target:
                i = mid
                break
            elif nums[mid] < target:
                l = mid+1
            else:
                r = mid-1
        if i is None:
            return [-1, -1]
        start = i
        end = i
        for s in range(i-1, -1, -1):
            if nums[s] == nums[i]:
                start = s
            else:
                break
        for e in range(i+1, len(nums)):
            if nums[e] == nums[i]:
                end = e
            else:
                break

        return [start, end]
