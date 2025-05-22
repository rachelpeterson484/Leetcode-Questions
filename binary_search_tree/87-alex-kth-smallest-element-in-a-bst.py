# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    visited_count = 0
    kthSmallestValue = 0

    def inorder(self, root, k):
        if not root:
            return

        self.inorder(root.left, k)

        self.visited_count += 1
        if self.visited_count == k:
            self.kthSmallestValue = root.val

        self.inorder(root.right, k)

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.inorder(root, k)
        return self.kthSmallestValue
