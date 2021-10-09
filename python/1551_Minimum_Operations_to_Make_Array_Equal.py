class Solution(object):
    def minOperations(self, n):
        """
        :type n: int
        :rtype: int
        """

        if n == 1:
            return 0

        if n % 2 == 0:
            goal = n - 1

            operations = 1

            tmp_operation = 1
            while tmp_operation < goal:
                tmp_operation += 2

                operations += tmp_operation

        else:
            goal = n - 1

            operations = 2
            tmp_operation = 2

            while tmp_operation < goal:
                tmp_operation += 2

                operations += tmp_operation

        return operations