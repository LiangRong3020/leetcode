class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        length1= len(num1)
        length2= len(num2)
        max_length= max(length1, length2)+1

        result_string= ''
        add_one= False
        for i in range(1, max_length):

            tmp1= 0 if i > length1 else int(num1[-i])
            tmp2 = 0 if i > length2 else int(num2[-i])

            sum_= tmp1+tmp2+1 if add_one else tmp1+tmp2
            if sum_ >= 10:
                add_one= True
                result_string= str(sum_%10) + result_string
            else:
                add_one = False
                result_string = str(sum_) + result_string

        return ('1'+ result_string) if add_one else result_string
