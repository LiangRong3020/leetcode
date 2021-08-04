# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    def check_if_target(self, node, target):
        if node.val == target.val:
            return node

        if node.left:
            tmp_left = self.check_if_target(node.left, target)
            if tmp_left:
                return tmp_left

        if node.right:
            tmp_right = self.check_if_target(node.right, target)
            if tmp_right:
                return tmp_right

        return None

    def getTargetCopy(self, original, cloned, target):
        """
        :type original: TreeNode
        :type cloned: TreeNode
        :type target: TreeNode
        :rtype: TreeNode
        """

        return self.check_if_target(cloned, target)