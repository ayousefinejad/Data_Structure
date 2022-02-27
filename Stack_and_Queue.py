# Arshia_yousefinezhad

class Stack:
    class Node:
        def __init__(self, data, after):
            self._data = data
            self._next = after
    def __init__(self):
        self._head = None
        self._size = 0

    def is_empty(self):
        return self._size == 0

    def add2first(self, p):
        node = self.Node(p, None)
        if self.is_empty():
            self._head = node
        else:
            node._next = self._head
            self._head = node
        self._size += 1

    def removefirst(self):
        tmp = self._head
        if self.is_empty():
            return None
        else:
            if self._size == 1:
                self._head = None
                self._size -= 1
                return tmp._data
            else:
                self._head = self._head._next
                self._size -= 1
                return tmp._data

    def top(self):
        if self.is_empty():
            return None
        return self._head._data

    def show(self):
        tmp = self._head
        while tmp != None:
            print(tmp._data, end='  -> ')
            tmp=tmp._next
        print()



class Queue:
    class Node:
        def __init__(self, element, left, right):
            self._element = element
            self._left = left
            self._right = right

    def __init__(self):
        self._header = self.Node(0, None, None)
        self._size = 0

    def is_empty(self):
        return self._header._element == 0

    def add2last(self, p):
        node = self.Node(p, None, None)
        if self.is_empty():
            self._header._left = node
            self._header._right = node
        else:
            node._left = self._header._right._left
            self._header._right._right = node
            self._header._right = node
        self._header._element += 1
        self._size += 1

    def removefirst(self):
        if self.is_empty():
            return None
        else:
            if self._size == 1:
                tmp = self._header._left
                self._header._left = None
                self._header._right = None
                self._header._element -= 1
                self._size -= 1
                return tmp._element
            else:
                tmp = self._header._left
                self._header._left = self._header._left._right
                self._header._element -= 1
                self._size -= 1
                return tmp._element

    def show(self):
        tmp = self._header._left
        if self.is_empty():
            return None
        else:
            while tmp != None:
                print(tmp._element, end=' <-> ')
                tmp=tmp._right
        print()


if __name__ == '__main__':
    st1 = Stack()
    st2 = Stack()
    q = Queue()
    lst = []
    # N = int(input("Queue length: "))
    # for i in range(N):
    #     a = int(input("Enter Number: "))
    #     lst.append(a)
    # print("Non-sort", end=' : ')
    lst.append([1,4, 7])
    lst.append([3,6, 9])
    lst.append([100,0, 9])
    lst.append([2,5, 8])
    print(lst)
    lst.sort()
    print(lst)

    while True:
        if len(lst) == 0:
            break
        else:
            m = lst.pop(0)
            if st1._size == 0:
                st1.add2first(m)
            else:
                while m < st1.top():
                    k = st1.removefirst()
                    st2.add2first(k)
                    if st1._size == 0:
                        break

                st1.add2first(m)
                while st2._size != 0:
                    n = st2.removefirst()
                    st1.add2first(n)

    for k in range(st1._size):
        e = st1.removefirst()
        lst.append(e)

    print("sort    ", end=' : ')
    print(lst)