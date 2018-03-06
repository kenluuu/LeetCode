class Solution:
    # @param {integer[]} nums
    # @return {string}
    def largestNumber(self, nums):
        def comp(x, y):
            if x+y > y+x:
                return 1
            elif x+y < y+x:
                return -1
            else:
                return 0

        nums = map(str, nums)
        nums.sort(cmp=comp, reverse=True)
        return str(int(''.join(nums)))
