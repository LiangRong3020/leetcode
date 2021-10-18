# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):

    def get_node_detail(self, nodes, parents=None, step=0):

        left_dict = {}
        right_dict = {}
        if nodes.left:
            left_dict = self.get_node_detail(nodes.left, nodes.val, step + 1)

        if nodes.right:
            right_dict = self.get_node_detail(nodes.right, nodes.val, step + 1)

        left_dict.update(right_dict)
        left_dict[nodes.val] = (parents, step)

        return left_dict

    def isCousins(self, root, x, y):
        """
        :type root: TreeNode
        :type x: int
        :type y: int
        :rtype: bool
        """

        node_dict = self.get_node_detail(root)

        if node_dict[x][0] != node_dict[y][0] and node_dict[x][1] == node_dict[y][1]:
            return True
        return False