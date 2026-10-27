class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def insert(root,data):
    if root is None:
        return Node(data)
    if data<root.data:
        root.left=insert(root.left,data)
    if data>root.data:
        root.right=insert(root.right,data)
    return root

def level_order(root):
    if root is None:
        return
    queue=[root]

    while queue:
        current=queue.pop(0)
        print(current.data,end=" ")
        if current.left is not None:
            queue.append(current.left)
        if current.right is not None:
            queue.append(current.right)

def copy_tree(root):
    if root is None:
        return None
    new_node=Node(root.data)
    new_node.left=copy_tree(root.left)
    new_node.right=copy_tree(root.right)
    return new_node

def height(root):
    if root is None:
        return 0
    left_height=height(root.left)
    right_height=height(root.right)
    return max(left_height,right_height)+1


root=None
n=int(input("Enter the number of Nodes:"))
for i in range(n):
    data=int(input("Enter the data of Node:"))
    root=insert(root,data)
print("Original BST Level Order:")
level_order(root)

new_root = copy_tree(root)

print("\nCopied BST Level Order:")
level_order(new_root)

print("\nHeight:", height(root))
