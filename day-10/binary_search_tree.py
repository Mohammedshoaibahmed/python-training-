
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def inorder(root):
    if root==None:
        return
    inorder(root.left)
    print(root.data,end=' ')
    inorder(root.right)

def BSTinsert(val, root):
    if root is None:
        return Node(val)
    if val < root.data:
        root.left = BSTinsert(val, root.left)
    else:
        root.right = BSTinsert(val, root.right)
    return root

n = int(input("Enter the number of nodes:"))
if n > 0:
    root = Node(int(input("Enter the root node:")))
    for _ in range(n - 1):
        val = int(input())
        root = BSTinsert(val, root)
    inorder(root)
else:
    print("The number of nodes must be greater than 0.")
