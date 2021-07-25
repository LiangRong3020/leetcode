class Solution(object):
    def numberOfMatches(self, n):
        """
        :type n: int
        :rtype: int
        """

        total_matches = 0

        while n > 1:
            tmp_matchs = n // 2
            total_matches += tmp_matchs
            n = n - tmp_matchs

        return total_matches