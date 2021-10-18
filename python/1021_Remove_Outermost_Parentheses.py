class Solution(object):
    def removeOuterParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """

        new_string = ''
        tmp_string = ''

        left = 0
        right = 0
        for s_ in s:
            tmp_string += s_

            if s_ == '(':
                left += 1

            else:
                right += 1

            if left == right:
                left = 0
                right = 0
                new_string += tmp_string[1:-1]
                tmp_string = ''

        return new_string