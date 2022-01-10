class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """

        a_list = list(a)
        b_list = list(b)

        add_ = 0

        finnal_list = []
        while (a_list and b_list) or add_ > 0:
            a_tmp = int(a_list.pop()) if a_list else 0
            b_tmp = int(b_list.pop()) if b_list else 0

            tmp_added = a_tmp + b_tmp + add_

            if tmp_added == 0:
                finnal_list = ['0'] + finnal_list
                add_ = 0
            elif tmp_added == 1:
                finnal_list = ['1'] + finnal_list
                add_ = 0
            elif tmp_added == 2:
                finnal_list = ['0'] + finnal_list
                add_ = 1
            elif tmp_added == 3:
                finnal_list = ['1'] + finnal_list
                add_ = 1

        if not (a_list or b_list):
            return ''.join(finnal_list)

        if a_list:
            finnal_list = a_list + finnal_list
            return ''.join(finnal_list)
        if b_list:
            finnal_list = b_list + finnal_list
            return ''.join(finnal_list)
