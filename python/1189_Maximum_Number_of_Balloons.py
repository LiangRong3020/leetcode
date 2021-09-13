
class Solution(object):
    def maxNumberOfBalloons(self, text, demo_text= 'balloon'):
        """
        :type text: str
        :rtype: int
        """
        record_dict= {}
        count_dict= {}
        for d in demo_text:

            if d in count_dict:
                count_dict[d] += 1
                continue

            count_dict[d]= 1
            record_dict[d]= 0

        for t in text:
            if t not in demo_text:
                continue

            record_dict[t] += 1

        minma= 10**4

        for k, v in record_dict.items():

            tmp_val= v // count_dict[k]
            minma = min(minma, tmp_val)

        return minma
