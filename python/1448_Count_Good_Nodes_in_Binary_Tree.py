# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):

    def goodNodes(self, root, record_list=[]):
        """
        :type root: TreeNode
        :rtype: int
        """

        count_good = 1 if record_list == [] or (max(record_list) <= root.val) else 0

        tmp_list = record_list + [root.val]
        if root.left:
            left_good = self.goodNodes(root.left, tmp_list)
            count_good += left_good

        if root.right:
            right_good = self.goodNodes(root.right, tmp_list)
            count_good += right_good

        return count_good