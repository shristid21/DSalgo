class BST:
    def __init__(self, key):
        self.key = key
        self.lchild = None
        self.rchild = None

  # insertion on BST
    def insert(self, data):
        if self.key is None:
            self.key = data
        if self.key == data:
            return
        if self.key > data:
            if self.lchild:
                self.lchild.insert(data)
            else:
                self.lchild = BST(data)

        if self.key < data:
            if self.rchild:
                self.rchild.insert(data)
            else:
                self.rchild = BST(data)
              
# preorser traversal
    def preorder(self):
        print(self.key)
        if self.lchild:
            self.lchild.preorder()
        if self.rchild:
            self.rchild.preorder()

  # inorder traversal
    def inorder(self):
        if self.lchild:
            self.lchild.inorder()
        print(self.key)
        if self.rchild:
            self.rchild.inorder()

  # postorder traversal
    def postorder(self):
        if self.lchild:
            self.lchild.preorder()
        if self.rchild:
            self.rchild.preorder()
        print(self.key)

  # search particular node in BST
    def search(self, data):
        if self.key == data:
            print("node is found")
        if data < self.key:
            if self.lchild:
                self.lchild.search(data)
            else:
                print("node not found")
        if data > self.key:
            if self.rchild:
                self.rchild.search(data)
            else:
                print("node not found")

  # deletion in BST
    def delete(self, data, curr):
            if self.key is None:
                print("tree is empty")
                return
        if data < self.key:
            if self.lchild:
                self.lchild = self.lchild.delete(data, curr)
            else:
                print("node not present")
        elif data > self.key:
            if self.rchild:
                self.rchild = self.rchild.delete(data, curr)
            else:
                print("node not present")
        else:
            if self.lchild is None:
                temp = self.rchild
                if data == curr:
                    self.key = temp.key
                    self.lchild = temp.lchild
                    self.rchild = temp.rchild
                    temp = None
                    return

                # self = None
                return temp
            if self.rchild is None:
                temp = self.lchild
                if data == curr:
                    self.key = temp.key
                    self.lchild = temp.lchild
                    self.rchild = temp.rchild
                    temp = None
                    return
                # self = None
                return temp
            node = self.rchild
            while node.lchild:
                node = node.lchild
            self.key = node.key
            self.rchild = self.rchild.delete(node.key, curr)

        return self


def count(node):
    if node is None:
        return 0
    return 1 + count(node.lchild) + count(node.rchild)


root = BST(None)
root.insert(20)
list1 = [1, 10, 80, 40, 50, 100]
for i in list1:
    root.insert(i)
# root.preorder()

print("height =", root.height())

