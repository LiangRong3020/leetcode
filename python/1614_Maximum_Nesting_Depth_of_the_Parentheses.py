class Solution(object):
    def maxDepth(self, s):
        """
        :type s: str
        :rtype: int
        """

        record_nested = 0
        max_nested = 0
        for s_ in s:

            if s_ == '(':
                record_nested += 1
                max_nested = max(max_nested, record_nested)

            elif s_ == ')':
                record_nested -= 1

        return max_nested