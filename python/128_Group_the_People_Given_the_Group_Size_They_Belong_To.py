import collections

class Solution(object):
    def groupThePeople(self, groupSizes):
        """
        :type groupSizes: List[int]
        :rtype: List[List[int]]
        """
        record_dict= collections.defaultdict(list)

        result_list= []
        for index_, value in enumerate(groupSizes):
            record_dict[value].append(index_)
            if len(record_dict[value]) == value:
                result_list.append(record_dict[value])
                record_dict[value]= []

        return result_list
