# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """

        maxma = n + 1
        minma = -1

        while True:
            guess_num = (maxma + minma) // 2

            guess_resule = guess(guess_num)

            if guess_resule == 0:
                return guess_num

            elif guess_resule == -1:
                maxma = guess_num

            else:
                minma = guess_num