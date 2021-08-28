import math

class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """

        helf_number= c // 2

        s= 0

        while s ** 2 <= helf_number:
            if math.sqrt(c- s ** 2) % 1 == 0:
                return True

            s += 1

        return False


