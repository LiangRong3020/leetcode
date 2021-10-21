import random

class RandomizedSet(object):

    def __init__(self):
        self.data_list = []

    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val in self.data_list:
            return False

        self.data_list += [val]
        return True

    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if not val in self.data_list:
            return False

        self.data_list.remove(val)

        return True

    def getRandom(self):
        """
        :rtype: int
        """

        random.shuffle(self.data_list)

        return self.data_list[0]

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()