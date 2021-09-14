import string


class Solution(object):
    def reverseOnlyLetters(self, s):
        """
        :type s: str
        :rtype: str
        """

        new_s= list(s)

        ori_s_num= len(s) -1
        replace_s_num= 0

        while ori_s_num >= 0:

            if s[ori_s_num] not in string.ascii_letters:
                ori_s_num -= 1

                continue

            if s[replace_s_num] not in string.ascii_letters:
                replace_s_num += 1
                continue

            new_s[replace_s_num] = s[ori_s_num]
            ori_s_num -= 1
            replace_s_num += 1

        return ''.join(new_s)
