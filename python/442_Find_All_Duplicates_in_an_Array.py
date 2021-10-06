class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        exist_set = set()
        duplicate_list = []
        for n in nums:
            if n in exist_set:
                duplicate_list.append(n)
            else:
                exist_set.add(n)

        return duplicate_list
