# arshia_yousefinezhad
# in the name of God

class DoubleLinked:
    class BST:
        class nodeBST:
            def __init__(self, key):
                self.KEY = key
                self.left = None
                self.right = None

        def __init__(self):
            self.root = None
            self.node = self

        def LVR(self):
            print("Postorder (LVR)")
            self.tmp_LVR(self.root)
            print()

        def tmp_LVR(self, parent):
            if parent == None:
                pass
            else:
                self.tmp_LVR(parent.left)
                print(parent.KEY, end=" => ")
                self.tmp_LVR(parent.right)

    class _Node:
        def __init__(self, element, left, right):
            self._element = element
            self._left = left
            self._right = right

    def __init__(self):
        self._header = self._Node(0, None, None)
        self._tree = self.BST()

    def is_empty(self):
        return self._header._element == 0

    def add2stack(self, header):
        node = self._Node(header, None, None)
        if self.is_empty():
            self._header._left = node
            self._header._right = node

        else:
            node._right = self._header._left
            self._header._left._left = node
            self._header._left = node
        self._header._element += 1

    def removefirst(self):
        if self.is_empty():
            return None
        else:
            tmp = self._header._left
            if self._header._element == 1:
                self._header._right = None
                self._header._left = None
            else:
                self._header._left = self._header._left._right
                self._header._left._left = None
            self._header._element -= 1
            return tmp._element

    def show_d(self):
        if self.is_empty():
            return None
        tmp = self._header._left
        while tmp != None:
            print(tmp._element, end=' -> ')
            tmp = tmp._right
        print()


if __name__ == '__main__':
    L = DoubleLinked()
    T = L._tree
    # name = str(input("Enter Operation: "))
    name = 'ab+cde+**'
    for i in name:
        if i == '+' or i == '*' or i == '/' or i == '-':
            T.root = T.nodeBST(i)
            R2 = L.removefirst()
            R1 = L.removefirst()
            if type(R1) == type(T.root):
                T.root.left = R1
            else:
                T.root.left = T.nodeBST(R1)

            if type(R2) == type(T.root):
                T.root.right = R2
            else:
                T.root.right = T.nodeBST(R2)
            L.add2stack(T.root)
        else:
            L.add2stack(i)
    T.LVR()