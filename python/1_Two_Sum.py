class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        for i, v in enumerate(nums):
            if v > target:
                continue
            seek_num= int(target-v)

            if seek_num in nums[i+1:]:
                new_index= nums[i + 1:].index(seek_num)+i+1
                return (i, new_index)

