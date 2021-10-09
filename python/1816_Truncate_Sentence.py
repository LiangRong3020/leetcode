class Solution(object):
    def truncateSentence(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        string_list = s.split(' ')

        return ' '.join(string_list[:k])