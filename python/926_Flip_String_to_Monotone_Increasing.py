class Solution(object):
    def minFlipsMonoIncr(self, s):
        """
        :type s: str
        :rtype: int
        """
        s_list = [0]
        for x in s:
            s_list.append(s_list[-1] + int(x))

        s_list_length = len(s_list)
        s_length= len(s)

        flips_list = [s_list[i] + s_length - i - (s_list[-1] - s_list[i]) for i in range(s_list_length)]

        return min(flips_list)

