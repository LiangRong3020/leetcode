
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        height_length= len(height)
        start= 0
        end= height_length-1

        start_max = 0
        end_max = 0

        record_water= 0
        while start < end:
            if height[start] < height[end]:
                if height[start] > start_max:
                    start_max = height[start]
                else:
                    record_water += (start_max- height[start])

                start += 1
            else:
                if height[end] > end_max:
                    end_max = height[end]
                else:
                    record_water += (end_max - height[end])

                end -= 1

        return record_water


#
# class Solution(object):
#     def trap(self, height):
#         """
#         :type height: List[int]
#         :rtype: int
#         """
#
#         record_water= 0
#         pre_max= 0
#         left_bound= len(height) -1
#         for i, v in enumerate(height):
#             # print(i, v, pre_max)
#             if pre_max != v and pre_max != 0 and i < left_bound:
#                 tmp_calcute= (min(max(height[i+1:]), pre_max) - v)
#                 if tmp_calcute > 0:
#                     record_water += tmp_calcute
#             pre_max = max(pre_max, v)
#
#         return record_water