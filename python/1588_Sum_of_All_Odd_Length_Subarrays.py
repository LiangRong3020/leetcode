class Solution(object):
    def sumOddLengthSubarrays(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        arr_length= len(arr)
        start_length= 3

        total_sum= sum(arr)
        while start_length < (arr_length+1):

            s_= 0
            e_= start_length
            while e_ <= arr_length:
                total_sum += sum(arr[s_:e_])

                s_ +=1
                e_ +=1

            start_length+= 2

        return total_sum