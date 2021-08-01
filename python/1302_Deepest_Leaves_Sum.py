# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):

    def find_deeplevel(self, node, level_):
        left_deep = None
        right_deep = None

        deep_level_right = 0
        deep_level_left = 0

        if node.left == None and node.right == None:
            return node.val, level_

        if node.left:
            left_deep, deep_level_left = self.find_deeplevel(node.left, level_ + 1)

        if node.right:
            right_deep, deep_level_right = self.find_deeplevel(node.right, level_ + 1)

        if deep_level_right == deep_level_left:
            return (left_deep + right_deep), deep_level_right
        elif deep_level_right > deep_level_left:
            return right_deep, deep_level_right
        else:
            return left_deep, deep_level_left

    def deepestLeavesSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        deepest_val, deepest_level = self.find_deeplevel(root, 1)

        return deepest_val
