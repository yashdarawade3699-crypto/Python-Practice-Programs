class Node:
    def __init__(self,id):
        self.id=id
        self.left=None
        self.right=None
def insert(root,id):
    if root is None:
        return Node(id)

    if id<root.id:
        root.left=insert(root.left,id)
    if id>root.id:
        root.right=insert(root.right,id)
    return root

def level_order(root):
    if root is None:
        return
    queue=[root]

    while queue:
        current=queue.pop(0)
        print(current.id,end=' ')
        if current.left is not None:
            queue.append(current.left)
        if current.right is not None:
            queue.append(current.right)


def copy_tree(root):
    if root is None:
        return None

    new_node=Node(root.id)
    new_node.left=copy_tree(root.left)
    new_node.right=copy_tree(root.right)
    return new_node

def height(root):
    if root is None :
        return 0
    left=height(root.left)
    right=height(root.right)
    return max(left,right)+1

root=None

n=int(input("Enter the number of nodes: "))

for i in range(n):
    id=int(input("Enter the id: "))
    root=insert(root,id)

print("Level Order Traversal")
level_order(root)
print("\nHeight Traversal")
print(height(root))
new_root=copy_tree(root)
print("\nCopy of the tree")
level_order(new_root)
