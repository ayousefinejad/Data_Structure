class BST:
    class BSTNode:
        class Element:
            def __init__(self, key, value):
                self.Key = key
                self.Value = value
# ---------------------------------------------------------------------------#
        def __init__(self, key, val):
            self.Data = self.Element(key, val)
            self.LeftChild=None
            self.RightChild=None
# ---------------------------------------------------------------------------#
        def getLeftChild(self):
            return self.LeftChild
#---------------------------------------------------------------------------#        
        def setLeftChild(self,left):
            self.LeftChild=left
#---------------------------------------------------------------------------#        
        def getRightChild(self):
            return self.RightChild
#---------------------------------------------------------------------------#        
        def setRightChild(self,right):
            self.RightChild=right
#---------------------------------------------------------------------------#        
        def getKey(self):
            return self.Data.Key
#---------------------------------------------------------------------------#        
        def setKey(self,k):
            self.Data.Key=k
#---------------------------------------------------------------------------#        
        def getValue(self):
            return self.Data.Value
#---------------------------------------------------------------------------#        
        def setKey(self,val):
            self.Data.Value=val
#---------------------------------------------------------------------------#            
        def minKey(self):
            if (self.LeftChild == None):
                return self.Data.Key
            else:
                return self.LeftChild.minKey()
#---------------------------------------------------------------------------#
        def remove(self,key,parent):
            print(self.Data.Key)
            if self.Data.Key > key:
                print("LeftChild:  self.Data.Key > key")
                if self.LeftChild != None:
                    return self.LeftChild.remove(key, self)
                else:
                    return None
            elif self.Data.Key<key:
                print("RightChild:  self.Data.Key < key")
                if self.RightChild!=None:
                    return self.RightChild.remove(key,self)
                else:
                    return None
            else:
                print("self.Data.Key = key")
                if self.RightChild != None and self.LeftChild != None:
                    self.Data.key = self.RightChild.minKey()
                    return self.RightChild.remove(self.Data.Key,self)
                elif parent.LeftChild == self:
                    if self.LeftChild != None:
                        parent.LeftChild = self.LeftChild
                    else:
                        parent.LeftChild = self.RightChild
                    return self

                elif parent.RightChild == self:
                    if self.LeftChild != None:
                        parent.RightChild = self.LeftChild
                    else:
                        parent.RightChild = self.RightChild
                    return self
# ---------------------------------------------------------------------------#
        def Search(self,key):
            if self.Data.Key == key:
                return True, self
            else:
                if self.Data.Key > key:
                    if self.LeftChild == None:
                        return False, None
                    else:
                        return self.LeftChild.Search(key)
                else:
                    if self.RightChild==None:
                        return False, None
                    else:
                        return self.RightChild.Search(key)
            return False, None
# ===========================================================================#
# ===========================================================================#
    def __init__(self):
        self.root=None
# ---------------------------------------------------------------------------#
    def addNode(self,key,val):
        if self.root == None:
            self.root=self.BSTNode(key,val)
        else:
            self.addNode1(self.root,key,val)
# ---------------------------------------------------------------------------#
    def addNode1(self,parent,key,val):
        cnode=parent
        print(type(cnode))
        if cnode.Data.Key==key:
            return None
        else:
            if cnode.Data.Key > key:
                if cnode.LeftChild == None:
                    cnode.LeftChild=self.BSTNode(key, val)
                    return cnode.LeftChild
                else:
                    self.addNode1(cnode.LeftChild, key, val)
            else:
                if cnode.RightChild==None:
                    cnode.RightChild=self.BSTNode(key, val)
                    return cnode.RightChild
                else:
                    self.addNode1(cnode.RightChild, key, val)
        return None
# ---------------------------------------------------------------------------#\
    def removeNode(self,key):
        if self.root==None:
            return None
        else:
            if self.root.getKey() == key:
                auxRoot=self.BSTNode(0, 0)
                auxRoot.setLeftChild(self.root)
                removedNode = self.root.remove(key, auxRoot)
                self.root = auxRoot.getLeftChild()
                if removedNode != None:
                    x=removedNode.getValue()
                    del removedNode
                    return x
                else:
                    return None
            else:
                removedNode = self.root.remove(key, None)
                if removedNode != None:
                    x=removedNode.getValue()
                    del removedNode
                    return x
                else:
                    return None
# ---------------------------------------------------------------------------#
    def searchNode(self,key):
        if self.root == None:
            return False
        else:
            return self.root.Search(key)
# ---------------------------------------------------------------------------#
    def PreOrderTmp(self,p):
        if p==None:
            pass 
        else:
            print('(%.0f,%d)'%(p.getKey(),p.getValue()),end=') => ')
            self.PreOrderTmp(p.getLeftChild())
            self.PreOrderTmp(p.getRightChild())

    def PreOrder(self,text):
        print(text,end=': ')
        self.PreOrderTmp(self.root)
        print()
# ---------------------------------------------------------------------------#
    def InOrderTmp(self,p):
        if p==None:
            pass 
        else:
            self.InOrderTmp(p.getLeftChild())
            # print('(%.0f,%d)'%(p.getKey(),p.getValue()),end=') => ')
            print(p.getKey(), end=' => ')
            self.InOrderTmp(p.getRightChild())
                
    def InOrder(self,text):
        print(text,end=': ')
        self.InOrderTmp(self.root)
        print()
# ---------------------------------------------------------------------------#
    def PostOrderTmp(self,p):
        if p==None:
            pass 
        else:
            self.PostOrderTmp(p.getLeftChild())
            self.PostOrderTmp(p.getRightChild())
            print('(%.0f,%d)'%(p.getKey(),p.getValue()),end=') => ')
                
    def PostOrder(self,text):
        print(text,end=': ')
        self.PostOrderTmp(self.root)
        print()

    def printt(self):
        print(self.root.getKey())
        print(self.root.getRightChild().getLeftChild().getKey())
        # print(self.root.getRightChild().getKey())
# ---------------------------------------------------------------------------#




if __name__ == '__main__':
    bst=BST()
    print(type(bst))
    bst.addNode(9,10)
    bst.addNode(1,34)
    bst.addNode(98,65)
    bst.addNode(-5,87)
    bst.addNode(10,90)
    bst.addNode(50,32)
    print(bst.root.Data.Key)

#     bst.InOrder('PostOrder')
    
#     (x,y)=bst.searchNode(98)
#     if x==True:
#         print('key=%d,value=%.f'%(y.getKey(),y.getValue()))
        
#     (x,y)=bst.searchNode(345)
#     if x==True:
#         print(y.getKey(),y.getValue())
    
    # bst.removeNode(9)
    # print(bst.removeNode(9))
#     bst.removeNode(1)
#     bst.PreOrder('PreOrder')
#     bst.InOrder('InOrder')
#     bst.PostOrder('PostOrder')





   





