class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        subset= [[]]
        seen_set= set()
        nums_length= len(nums)
        for i in range(nums_length):

            tmp_subset= subset[:]
            for s in tmp_subset:
                tmp_list= s[:]
                tmp_list.append(nums[i])
                new_string = ','.join([str(x) for x in tmp_list])
                if not new_string in seen_set:
                    subset.append(tmp_list)
                    seen_set.add(new_string)

        return subset
