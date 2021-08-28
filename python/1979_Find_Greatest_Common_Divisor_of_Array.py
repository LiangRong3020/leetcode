class Solution(object):
    def findGCD(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxma = max(nums)
        minima = min(nums)

        for i in range(minima, 0, -1):

            if (maxma % i == 0) and (minima % i == 0):
                return i

        return 1