# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):

    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        maxma = max(nums)
        max_index = nums.index(maxma)
        root = TreeNode(maxma)

        if len(nums[:max_index]) > 0:
            root.left = self.constructMaximumBinaryTree(nums[:max_index])

        if len(nums[max_index + 1:]) > 0:
            root.right = self.constructMaximumBinaryTree(nums[max_index + 1:])

        return root