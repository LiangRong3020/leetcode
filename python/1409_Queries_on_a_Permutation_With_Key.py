class Solution(object):
    def processQueries(self, queries, m):
        """
        :type queries: List[int]
        :type m: int
        :rtype: List[int]
        """
        p = [i for i in range(1, m + 1)]

        result = []
        for q in queries:
            index_ = p.index(q)
            result.append(index_)

            pop_number = p.pop(index_)
            p = [pop_number] + p

        return result