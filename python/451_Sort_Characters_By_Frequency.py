import collections, operator

class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """

        def zero():
            return 0
        record_dict= collections.defaultdict(zero)

        for s_ in s:
            record_dict[s_] += 1

        record_sort_list = sorted(record_dict.items(), key=operator.itemgetter(1), reverse=True)

        new_list= [x[0]*x[1] for x in record_sort_list]
        return ''.join(new_list)
