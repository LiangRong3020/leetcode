class Solution(object):
    def countKDifference(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        nums_length = len(nums)

        result = 0
        start = 0
        end = 1

        while start < nums_length:

            accept_list = [nums[start] + k, nums[start] - k]
            while end < nums_length:
                if nums[end] in accept_list:
                    result += 1

                end += 1
            start += 1
            end = start + 1

        return result