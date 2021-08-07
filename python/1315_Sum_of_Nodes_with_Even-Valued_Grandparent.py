# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):

    def search_node(self, node, record_parent):
        tmp_sum = 0
        if record_parent[1] % 2 == 0:
            tmp_sum = node.val

        if node.left:
            left_sum = self.search_node(node.left, (node.val, record_parent[0]))
            tmp_sum += left_sum
        if node.right:
            right_sum = self.search_node(node.right, (node.val, record_parent[0]))
            tmp_sum += right_sum

        return tmp_sum

    def sumEvenGrandparent(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        return self.search_node(root, (-1, -1))