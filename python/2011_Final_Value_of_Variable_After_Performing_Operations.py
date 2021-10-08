class Solution(object):
    def finalValueAfterOperations(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        increments = ['++X', 'X++']
        decrements = ['--X', 'X--']

        x = 0

        for operation in operations:
            if operation in increments:
                x += 1
            else:
                x -= 1

        return x

