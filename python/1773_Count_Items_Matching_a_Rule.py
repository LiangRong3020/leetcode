class Solution(object):
    def countMatches(self, items, ruleKey, ruleValue):
        """
        :type items: List[List[str]]
        :type ruleKey: str
        :type ruleValue: str
        :rtype: int
        """

        if ruleKey == 'type':
            query_index = 0
        elif ruleKey == 'color':
            query_index = 1
        else:
            query_index = 2

        count_ = 0
        for item in items:
            if item[query_index] == ruleValue:
                count_ += 1

        return count_
