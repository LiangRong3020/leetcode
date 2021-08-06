"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution(object):

    def collect_nodes(self, node, level):
        now_level_list = [(level, node.val)]
        if node.children == None:
            return now_level_list, level

        now_max = level
        for n in node.children:
            tmp_level_list, tmp_max = self.collect_nodes(n, level + 1)
            now_max = max(now_max, tmp_max)
            now_level_list += tmp_level_list

        return now_level_list, now_max

    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        if root == None:
            return []

        all_level_list, max_level = self.collect_nodes(root, 0)
        result_list = [[] for _ in range(max_level + 1)]

        for a in all_level_list:
            result_list[a[0]].append(a[1])

        return result_list