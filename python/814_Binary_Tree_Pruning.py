# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):

    def sum_node(self, node):
        total_ = node.val
        if node.left:
            tmp_sum = self.sum_node(node.left)
            if tmp_sum == 0:
                node.left = None
            total_ += tmp_sum
        if node.right:
            tmp_sum = self.sum_node(node.right)
            if tmp_sum == 0:
                node.right = None
            total_ += tmp_sum
        return total_

    def pruneTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """

        self.sum_node(root)
        if root.left == None and root.right == None and root.val == 0:
            return None
        return root

