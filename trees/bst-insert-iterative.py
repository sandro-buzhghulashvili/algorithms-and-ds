class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BST:
    def __init__(self):
        self.root = None

    def insert(self, val):
        if not self.root:
            self.root = TreeNode(val)
        else:
            cur = self.root
            parent = None

            while True:
                parent = cur

                if val < cur.val:
                    cur = cur.left
                    if not cur:
                        parent.left = TreeNode(val)
                        break
                else:
                    cur = cur.right
                    if not cur:
                        parent.right = TreeNode(val)
                        break
    

example_bst = BST();

example_bst.insert(12)
example_bst.insert(11)
example_bst.insert(13)

def in_order(node):
    if node:
        in_order(node.left)
        print(node.val)
        in_order(node.right)

in_order(example_bst.root)