import bisect

class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        nums_len= len(nums)
        if nums_len == 3:
            return sum(nums)

        now_min= 10**5
        now_record= None
        nums.sort()

        for i , v in enumerate(nums[:-2]):

            for j, x in enumerate(nums[i+1:-1]):

                tmp_sum= x+v
                except_num= target - tmp_sum


                left_bisect= bisect.bisect_left(nums[i+j+2:], except_num)+i+j+2
                bisect_list= [left_bisect, left_bisect-1] if except_num >= 0 else [left_bisect, left_bisect+1]

                for the_bisect in bisect_list:
                    the_bisect= nums_len-1 if the_bisect == nums_len else the_bisect
                    tmp_left_num= nums[the_bisect]+ tmp_sum
                    if the_bisect == i or the_bisect == i+j+1:
                        continue


                    if tmp_left_num == target:
                        return target

                    left_tmp_dff = abs(target-tmp_left_num)
                    if left_tmp_dff < now_min:
                        now_min= left_tmp_dff
                        now_record= tmp_left_num

        return now_record
