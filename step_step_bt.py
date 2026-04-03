# https://leetcode.com/problems/step-by-step-directions-from-a-binary-tree-node-to-another/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        def find_path(node, target, path):
            if not node:
                return False
            if node.val == target:
                return True
            path.append("L")
            if find_path(node.left, target, path):
                return True
            path.pop()
            path.append("R")
            if find_path(node.right, target, path):
                return True
            path.pop()
            return False

        path_to_s = []
        path_to_t = []
        find_path(root, startValue, path_to_s)
        find_path(root, destValue, path_to_t)
        i = 0
        while i < len(path_to_s) and i < len(path_to_t) and path_to_s[i] == path_to_t[i]:
            i += 1
        up_moves = 'U' * (len(path_to_s) - i)

        down_moves = ''.join(path_to_t[i:])

        return up_moves + down_moves
