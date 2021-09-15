
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def getDecimalValue(self, head):
        """
        :type head: ListNode
        :rtype: int
        """

        value_list = []
        count_list = []
        count_ = 0

        while head:
            value_list.append(head.val)
            count_list.append(count_)
            count_ += 1

            head = head.next

        result = 0
        for i, j in zip(value_list, count_list[::-1]):
            if i == 0:
                continue

            result += i * 2 ** j

        return result
