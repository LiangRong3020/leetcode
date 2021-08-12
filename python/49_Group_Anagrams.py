import collections

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        record_dict= collections.defaultdict(list)

        for s in strs:

            new_s= ''.join(sorted(s))
            record_dict[new_s].append(s)

        return record_dict.values()