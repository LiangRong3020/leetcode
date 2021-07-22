class Solution(object):
    def partitionDisjoint(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        now_min= 10^6
        nearly_max= nums[0]
        last_time_max_value = nums[0]
        last_time_max= -1
        record_list = []
        for i, v in enumerate(nums):
            nearly_max= max(nearly_max, v)
            if v <= now_min:
                if v != now_min:
                    record_list = []
                    last_time_max= -1

                now_min= v
                record_list.append((i,v,nearly_max))
                last_time_max_value= nearly_max
            elif v < last_time_max_value:
                last_time_max= i
                last_time_max_value= nearly_max


        if len(record_list) == 1:
            return max(record_list[0][0]+1, last_time_max+1)
        elif len(record_list) == 0:
            return max(1, last_time_max+1)
        elif record_list[0][1] == record_list[0][2]:
            return record_list[0][0]+1
        else:
            return max(record_list[-1][0] + 1, last_time_max+1)


