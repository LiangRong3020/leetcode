class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s_list = s.split(' ')[::-1]

        new_list = []

        for s2 in s_list:
            if not (s2 == '' or s2 == ' '):
                new_list.append(s2)

        return ' '.join(new_list)

