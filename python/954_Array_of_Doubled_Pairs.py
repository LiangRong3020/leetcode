class Solution(object):
    def canReorderDoubled(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """

        if len(arr) == 0:
            return True

        arr.sort()
        while arr:
            tmp_num= arr.pop(0)
            if tmp_num < 0:
                if tmp_num % 2 != 0:
                    return False
                oppi_num= tmp_num // 2
                if oppi_num in arr:
                    arr.remove(oppi_num)
                else:
                    return False

            else:
                oppi_num = tmp_num * 2
                if oppi_num in arr:
                    arr.remove(oppi_num)
                else:
                    return False

        return True

    