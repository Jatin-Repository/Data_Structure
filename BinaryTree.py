class BinaryTree:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.data = value

    def insert(self, value):
        if self.data:
            if value < self.data:
                if self.left is None:
                    self.left = BinaryTree(value)
                else:
                    self.left.insert(value)
            elif value > self.data:
                if self.right is None:
                    self.right = BinaryTree(value)
                else:
                    self.right.insert(value)
            else:
                self.data = value

    def PrintInorderTree(self):
        if self.left:
            self.left.PrintInorderTree()
        print(self.data, end=" ")
        if self.right:
            self.right.PrintInorderTree()

    def PrintPreorderTree(self):
        print(self.data, end=" ")
        if self.left:
            self.left.PrintPreorderTree()
        if self.right:
            self.right.PrintPreorderTree()

    def PrintPostorderTree(self):
        if self.left:
            self.left.PrintPostorderTree()
        if self.right:
            self.right.PrintPostorderTree()
        print(self.data, end=" ")


root = BinaryTree(54)
root.insert(17)
root.insert(23)
root.insert(100)
root.insert(13)

print("In_Order:")
root.PrintInorderTree()
print("\nPre_Order:")
root.PrintPreorderTree()
print("\nPost_Order:")
root.PrintPostorderTree()












