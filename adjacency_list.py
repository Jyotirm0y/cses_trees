class Node:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self,data):
        if self.data is None:
            self.data = data
        else:
            if data < self.data :
                if self.left is None:
                    self.left =Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                     self.right = Node(data)
                else:
                     self.right.insert(data)

def inorder(root):
    if root is None:
        return
    else:
        inorder(root.left)
        print(root.data, end=' ')
        inorder(root.right)

def Adjacency_List(root):
    if root is None:
        return
    else:
        d[root.data] =[]
        Adjacency_List(root.left)
        if root.left:
            d[root.data].append(root.left.data)
        if root.right:
            d[root.data].append(root.right.data)
        Adjacency_List(root.right)
    return d


if  __name__== '__main__':

    root=Node(5)
    root.insert(2)
    root.insert(3)
    root.insert(7)
    root.insert(10)
    # inorder(root)
    d={}

    a= Adjacency_List(root)
    for ele in a:
        print(f'{ele}:{a[ele]}')

