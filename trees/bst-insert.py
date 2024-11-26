class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BST:
    def __init__(self):
        self.root = None

    def insert(self, root, val):
        if root is None:
            return TreeNode(val)
        
        if val < root.val:
            root.left = self.insert(root.left, val)
        elif val > root.val:
            root.right = self.insert(root.right, val)
        
        return root

    def add(self, val):
        self.root = self.insert(self.root, val)

    def in_order(self, root):
        if root:
            self.in_order(root.left)
            print(root.val, end=" ")
            self.in_order(root.right)

    def print_in_order(self):
        self.in_order(self.root)
        print() 


example_bst = BST()
example_bst.add(12)
example_bst.add(10)
example_bst.add(15)

example_bst.print_in_order()  
