# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):

    def sum_node(self, node, low, high):

        if node.val >= low and node.val <= high:

            tmp_sum = node.val
        else:
            tmp_sum = 0

        if node.val >= low:
            if node.left:
                tmp_left = self.sum_node(node.left, low, high)
                tmp_sum += tmp_left

        if node.val <= high:
            if node.right:
                tmp_right = self.sum_node(node.right, low, high)
                tmp_sum += tmp_right

        return tmp_sum

    def rangeSumBST(self, root, low, high):
        """
        :type root: TreeNode
        :type low: int
        :type high: int
        :rtype: int
        """
        return self.sum_node(root, low, high)
