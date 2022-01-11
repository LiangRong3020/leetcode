# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):

    def get_path(self, node, path_):

        path_ += str(node.val)
        all_path = []

        if node.left:
            left_ = self.get_path(node.left, path_)
            all_path += left_

        if node.right:
            right_ = self.get_path(node.right, path_)
            all_path += right_

        if not (node.left or node.right):
            all_path += [path_]

        return all_path

    def sumRootToLeaf(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        all_path = self.get_path(root, '')

        total = 0

        for p in all_path:
            total += int(p, 2)

        return total

