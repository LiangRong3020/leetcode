class Solution(object):
    def minPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        nums.sort()

        nums_length = len(nums)
        pair_sum_list = []

        for i in range(nums_length):
            j = -1 * (i + 1)

            pair_sum_list.append((nums[i] + nums[j]))

        return max(pair_sum_list)