from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def isValid(node, minVal, maxVal):
            if not node: 
                return True
            if not (minVal < node.val < maxVal):  
                return False
            return isValid(node.left, minVal, node.val) and isValid(node.right, node.val, maxVal)

        return isValid(root, float('-inf'), float('inf'))

