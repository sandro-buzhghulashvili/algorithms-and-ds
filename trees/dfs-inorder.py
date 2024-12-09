from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def inorder(root):
            if root:
                inorder(root.left)
                res.append(root.val)
                inorder(root.right)
            
        inorder(root)
        return res
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def preorder(root):
            if root:
                res.append(root.val)
                preorder(root.left)
                preorder(root.right)
            
        preorder(root)
        return res
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def postorder(root):
            if root:
                postorder(root.left)
                postorder(root.right)
                res.append(root.val)

            
        postorder(root)
        return res
    def reverseorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def reverseorder(root):
            if root:
                reverseorder(root.right)
                res.append(root.val)
                reverseorder(root.left)
            
        reverseorder(root)
        return res