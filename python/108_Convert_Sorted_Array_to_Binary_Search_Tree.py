# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):

    def build_a_balance_tree(self, nums, start, end):
        if start > end:
            return None
        mid = start+(end - start) // 2
        node = TreeNode(nums[mid])
        node.left = self.build_a_balance_tree(nums, start, (mid - 1))
        node.right = self.build_a_balance_tree(nums, (mid + 1), end)

        return node

    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        return self.build_a_balance_tree(nums, 0, len(nums)-1)



tt=Solution()
nums = [-10,-3,0,5,9]

tt.sortedArrayToBST(nums)