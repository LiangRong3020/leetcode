class Solution(object):
    def createTargetArray(self, nums, index):
        """
        :type nums: List[int]
        :type index: List[int]
        :rtype: List[int]
        """

        nums_length = len(nums)
        target = []
        for i in range(nums_length):
            target.insert(index[i], nums[i])

        return target