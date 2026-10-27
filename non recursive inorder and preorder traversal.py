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
    if root.right>data:
            root.right =insert(root.right,data)
    return root

def preorder(root):
        if root is None:
            return
        stack=[root]

        while stack:
            current=stack.pop()
            print(current.stack, end=" ")

            if current.right is not None:
                stack.append(current.right)
            if current.left is not None:
                stack.append(current.left)


root= None
n=int(input("Enter the value of Nodes:"))

for i in range(n):
    data=int(input("Enter the value:"))
    root=insert(root,data)
print("Preorder Traversal")
preorder(root)



