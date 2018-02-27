class Solution(object):
    def twoSum(self, nums, target):

        dict = {}
        for i in range(len(nums)):
            complementary = target - nums[i]
            if complementary in dict:
                return [dict[complementary], i]
            else:
                dict[nums[i]] = i
