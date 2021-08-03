class Solution(object):
    def interpret(self, command):
        """
        :type command: str
        :rtype: str
        """
        command = command.replace('(al)', 'al').replace('()', 'o')
        return command
