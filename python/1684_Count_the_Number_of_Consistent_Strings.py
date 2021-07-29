class Solution(object):
    def countConsistentStrings(self, allowed, words):
        """
        :type allowed: str
        :type words: List[str]
        :rtype: int
        """

        count_ = 0
        for word in words:
            tmp_set = set(word)
            is_allow = True

            for w in tmp_set:
                if w not in allowed:
                    is_allow = False
                    break

            if is_allow:
                count_ += 1

        return count_