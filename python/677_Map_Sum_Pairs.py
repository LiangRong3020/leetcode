class MapSum(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.record_ = {}

    def insert(self, key, val):
        """
        :type key: str
        :type val: int
        :rtype: None
        """
        self.record_[key] = val

    def sum(self, prefix):
        """
        :type prefix: str
        :rtype: int
        """
        prefix_length = len(prefix)
        sum_ = 0
        for k, v in self.record_.items():
            if k[:prefix_length] == prefix:
                sum_ += v

        return sum_