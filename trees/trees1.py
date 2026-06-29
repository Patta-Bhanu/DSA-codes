from collections import deque

class TreeNode:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class BinaryTree:

    def __init__(self):
        self.root = None

    def preorder(self, root):

        if root is None:
            return

        print(root.val, end=" ")

        self.preorder(root.left)
        self.preorder(root.right)

    def inorder(self, root):

        if root is None:
            return

        self.inorder(root.left)

        print(root.val, end=" ")

        self.inorder(root.right)

    def postorder(self, root):

        if root is None:
            return

        self.postorder(root.left)
        self.postorder(root.right)

        print(root.val, end=" ")

    def levelorder(self):

        if self.root is None:
            return

        q = deque()
        q.append(self.root)

        while q:

            node = q.popleft()

            print(node.val, end=" ")

            if node.left:
                q.append(node.left)

            if node.right:
                q.append(node.right)


bt = BinaryTree()

bt.root = TreeNode(1)

bt.root.left = TreeNode(2)
bt.root.right = TreeNode(3)

bt.root.left.left = TreeNode(4)
bt.root.left.right = TreeNode(5)

bt.root.right.left = TreeNode(6)
bt.root.right.right = TreeNode(7)

print("Preorder Traversal")
bt.preorder(bt.root)

print("\n")

print("Inorder Traversal")
bt.inorder(bt.root)

print("\n")

print("Postorder Traversal")
bt.postorder(bt.root)

print("\n")

print("Level Order Traversal")
bt.levelorder()