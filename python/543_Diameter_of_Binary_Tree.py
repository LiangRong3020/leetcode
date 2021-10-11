# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):

    def get_length(self, nodes):

        left = 0
        right = 0
        max_left = 0
        max_right = 0
        if nodes.left:
            left, max_left = self.get_length(nodes.left)

        if nodes.right:
            right, max_right = self.get_length(nodes.right)

        max_length = left + right

        return max(left, right) + 1, max([max_length, max_left, max_right])

    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        max_length, max_diameter = self.get_length(root)

        return max_diameter