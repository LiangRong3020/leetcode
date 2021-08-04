# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):

    def check_nodes(self, nodes, targetSum, tmp_list):
        now_list = tmp_list[:]
        now_list.append(nodes.val)
        if nodes.left == None and nodes.right == None:
            if sum(now_list) == targetSum:
                return [now_list]
            else:
                return []

        total_list = []
        if nodes.left:
            left_sum = self.check_nodes(nodes.left, targetSum, now_list)
            total_list += left_sum
        if nodes.right:
            right_sum = self.check_nodes(nodes.right, targetSum, now_list)
            total_list += right_sum

        return total_list

    def pathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: List[List[int]]
        """
        if root == None:
            return []
        return self.check_nodes(root, targetSum, [])