class Solution(object):
    def findingUsersActiveMinutes(self, logs, k):
        """
        :type logs: List[List[int]]
        :type k: int
        :rtype: List[int]
        """

        record_dict = {}
        for log in logs:
            if log[0] in record_dict:
                record_dict[log[0]].add(log[1])

            else:
                record_dict[log[0]] = set([log[1]])

        result_list = [0 for _ in range(k)]

        for r in record_dict:
            tmp_index = len(record_dict[r]) - 1
            result_list[tmp_index] += 1

        return result_list
