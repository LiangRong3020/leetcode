class Solution(object):
    def countGoodTriplets(self, arr, a, b, c):
        """
        :type arr: List[int]
        :type a: int
        :type b: int
        :type c: int
        :rtype: int
        """

        arr_length = len(arr)
        f = 0
        s = 1
        t = 2

        result_pair = 0

        while f < arr_length:

            s = f + 1

            while s < arr_length:

                t = s + 1

                while t < arr_length:
                    if abs(arr[f] - arr[s]) <= a and abs(arr[s] - arr[t]) <= b and abs(arr[f] - arr[t]) <= c:
                        result_pair += 1

                    t += 1

                s += 1

            f += 1

        return result_pair