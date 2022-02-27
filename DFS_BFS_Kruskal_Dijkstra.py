# Arshia_yousefinezhad
# In The name Of God

from collections import defaultdict
class Data:
    def __init__(self, vertex, Edge):
        self.ver = vertex
        self.Edge = Edge
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
        def __init__(self, data, after):
            self._data = data
            self._next = after
    def __init__(self):
        self._head = None
        self._size = 0

    def is_empty(self):
        return self._size == 0

    def add2last(self, p):
        node = self.Node(p, None)
        if self.is_empty():
            self._head = node
        else:
            tmp = self._head
            while tmp._next != None:
                tmp = tmp._next
            tmp._next = node
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
            print('[',tmp._data.ver, ',', tmp._data.Edge,']',end='  -> ')
            tmp=tmp._next
        print()

    def show1(self):
        tmp = self._head
        while tmp != None:
            print(tmp._data,end='  -> ')
            tmp=tmp._next
        print()
class Graph:
    def __init__(self, v):
        self.v = v
        self.parent = []
        self.adj = defaultdict(list)
        for j in range(v):
            self.adj[j] = Queue()

    def addEdge(self, v, u, e):
        self.parent.append([e, v, u])
        d = Data(u, e)
        self.adj[v].add2last(d)

    def addVertex(self):
        last = self.v
        self.v += 1
        old = self.adj
        print(old[1])
        self.adj = defaultdict(list)
        for j in range(self.v):
            if j == last:
                self.adj[j] = Queue()
            else:
                self.adj[j] = old[j]

    def in_vertex(self, u):
        c = 0
        tmp = self.adj
        for i in range(self.v):
                tmp1 = tmp[i]._head
                for i in range(tmp[i]._size):
                    if tmp1._data.ver == u:
                        c += 1
                    tmp1=tmp1._next
        print("In_degree",u,': ', c)

    def out_vertex(self, v):
        print("out_degree",v,": ",self.adj[v]._size)

    def all_Edge(self):
        count = 0
        tmp = self.adj
        for i in range(self.v):
                tmp1 = tmp[i]._head
                for i in range(tmp[i]._size):
                    count += 1
                    tmp1=tmp1._next
        return count

    def BFS(self, v):
        tmp = self.adj
        visited = [False] * len(self.adj)
        queue = Queue()
        queue.add2last(v)
        visited[v] = True
        while queue._size != 0:
            v = queue.removefirst()
            print(v, end='->')
            tmp1 = tmp[v]._head
            for n in range(tmp[v]._size):
                if visited[tmp1._data.ver] is False:
                    queue.add2last(tmp1._data.ver)
                    visited[tmp1._data.ver] = True
                tmp1=tmp1._next

    def DFS(self, s):
        tmp = self.adj
        visited = [False] * self.v
        stack = Stack()   # probing
        stack.add2first(s)
        visited[s] = True
        print(s, end='->')
        while stack._size != 0:
            tmp1 = tmp[s]._head
            for i in range(tmp[s]._size):
                if visited[tmp1._data.ver] is False:
                    a = tmp1._data.ver
                    stack.add2first(a)
                    visited[a] = True
                    print(a, end='->')
                    s = stack.top()
                    break
                tmp1=tmp1._next
                if i == tmp[s]._size-1:
                    s = stack.top()
                    stack.removefirst()
        print()

    def minKey(self, key, Visited):
        little = 1000000
        for v in range(self.v):
            if key[v] < little and Visited[v] is False:
                little = key[v]
                min_index = v
        return min_index

    def kruskal(self):
        lst = []
        N = self.all_Edge()
        self.parent.sort()
        visited = [False] * self.v
        for i in range(N):
            if visited[self.parent[i][1]] is False or visited[self.parent[i][2]] is False:
                if visited[self.parent[i][1]] is False:
                    visited[self.parent[i][1]] = True
                if visited[self.parent[i][2]] is False:
                    visited[self.parent[i][2]] = True
                lst.append(self.parent[i])
        print("vertex", "\t\t", "Distance")
        for p in range(len(lst)):
            print(lst[p][1], '__', lst[p][2], "\t\t\t", lst[p][0])


    def dijkstra(self, ver):
        tmp = self.adj
        key = [100000] * self.v
        key[ver] = 0
        Visited = [False] * self.v
        for count in range(self.v):
            u = self.minKey(key, Visited)
            Visited[u] = True
            tmp1 = tmp[u]._head
            for v in range(tmp[u]._size):
                if key[tmp1._data.ver] > key[u] + tmp1._data.Edge:
                    if Visited[tmp1._data.ver] is False:
                        key[tmp1._data.ver] = key[u] + tmp1._data.Edge
                tmp1=tmp1._next
        print("Vertex \tDistance from", ver)
        for node in range(self.v):
            print(node, "\t\t\t", key[node])


if __name__ == '__main__':

    file = open('graph.txt', 'r')
    vertex = file.readline()
    Edge = file.readline()
    g = Graph(int(vertex))
    lst = []
    for i in range(int(Edge)):
        m = file.readline()
        r = m.split()
        lst.append(r)
    for t in lst:
        v = t[0]
        u = t[1]
        e = t[2]
        g.addEdge(int(v), int(u), int(e))
    file.close()

    for k, v in g.adj.items():
        print(k, ' ', end='->')
        v.show()
    print()
    g.in_vertex(1)
    g.out_vertex(2)
    print("all_Edge: ", g.all_Edge())
    print()
    print("BFS(0)", end=': ')
    g.BFS(0)
    print()
    print("DFS(0)", end=': ')
    g.DFS(0)
    print()
    print("------kruskal------")
    g.kruskal()
    print()

    print("------dijkstra------")
    g.dijkstra(1)
