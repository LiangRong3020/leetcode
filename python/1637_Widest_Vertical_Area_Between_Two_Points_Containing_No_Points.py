class Solution(object):
    def maxWidthOfVerticalArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """

        x_list = list(set([x[0] for x in points]))
        if len(x_list) == 1:
            return 0

        x_list.sort()

        range_list = [x_list[i + 1] - x_list[i] for i in range(len(x_list) - 1)]

        return max(range_list)
