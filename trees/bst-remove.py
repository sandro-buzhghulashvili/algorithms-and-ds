class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BST:
    def __init__(self):
        self.root = None

    def remove_element(self, val):
        self.root = remove(self.root, val)
    
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


example_bst = BST()
example_bst.add(12)
example_bst.add(10)
example_bst.add(15)


def findMinNode(root):
    curr = root

    while curr and curr.left:
        curr = curr.left
    
    return curr

def remove(root, val):
    if not root:
        return None
    
    if val < root.val:
        root.left = remove(root.left, val)
    elif val > root.val:
        root.right = remove(root.right, val)
    else:
        if not root.right:
            return root.left
        elif not root.left:
            return root.right
        else:
            min_node = findMinNode(root.right)
            root.val = min_node.val
            root.right = remove(root.right, min_node.val)
    return root
        

example_bst.remove_element(10)
example_bst.print_in_order()

