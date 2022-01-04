class Solution(object):
    def bitwiseComplement(self, n):
        """
        :type n: int
        :rtype: int
        """

        binary_num= bin(n)[2:]

        binary_lenght= len(binary_num)

        ans= 0
        for i in range(binary_lenght):
            if binary_num[i] == '0':
                ans += 2**(binary_lenght -1 -i)

        return ans

tt= Solution()
print(tt.bitwiseComplement(2))
