import string


class Solution(object):

    def shift(self, c, x):

        string_index= string.ascii_lowercase.index(c)
        return string.ascii_lowercase[(string_index+x)]

    def replaceDigits(self, s):
        """
        :type s: str
        :rtype: str
        """

        new_string= ''
        lowercase=  string.ascii_lowercase
        for s_ in s :

            if s_ in lowercase:
                new_string += s_

            else:
                new_string += self.shift(new_string[-1], int(s_))

        return new_string