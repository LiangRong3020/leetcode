# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        store_list = []

        while head:
            store_list.append(head)

            head = head.next

        store_length = len(store_list)

        helf = store_length // 2

        if store_length == 1:
            return store_list[0]

        return store_list[helf]