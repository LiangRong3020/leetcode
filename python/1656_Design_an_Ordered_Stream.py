class OrderedStream(object):

    def __init__(self, n):
        """
        :type n: int
        """
        self.data_list = ['' for _ in range(n + 1)]
        self.now_ = 1
        self.record_list = []

    def insert(self, idKey, value):
        """
        :type idKey: int
        :type value: str
        :rtype: List[str]
        """
        self.data_list[idKey] = value
        if self.now_ == idKey:

            new_key = idKey + 1
            while new_key in self.record_list:
                new_key += 1

            self.now_ = new_key
            return self.data_list[idKey:new_key]
        else:
            self.record_list.append(idKey)

# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)