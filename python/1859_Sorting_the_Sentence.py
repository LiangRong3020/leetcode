class Solution(object):
    def sortSentence(self, s):
        """
        :type s: str
        :rtype: str
        """
        s_list = s.split(' ')
        new_list = ['' for x in s_list]

        for s_ in s_list:
            s_index = int(s_[-1]) - 1
            new_list[s_index] = s_[:-1]

        return ' '.join(new_list)
