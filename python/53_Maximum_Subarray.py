class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        max_sum = (10 ** 4) * -1

        restart = True
        tmp_sum = (10 ** 4) * -1

        for n in nums:

            if restart:
                tmp_sum = n
                restart = False
            else:
                tmp_sum += n

            if tmp_sum > max_sum:
                max_sum = tmp_sum

            if tmp_sum < 0:
                restart = True
                tmp_sum = 10 ^ 4 * -1

        return max_sum