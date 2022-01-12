class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        saw_set = set()

        for n in nums:
            if n in saw_set:
                return True
            else:
                saw_set.add(n)

        return False

    